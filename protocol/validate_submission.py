#!/usr/bin/env python3
import datetime, json, pathlib, re, sys, urllib.parse

UUID = re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$")
TIMESTAMP = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,9})?(?:Z|[+-]\d{2}:\d{2})$")

def fail(message):
    print("OpenCat submission invalid: " + message, file=sys.stderr)
    raise SystemExit(1)

def text(value, label, low, high):
    if not isinstance(value, str): fail(label + " must be a string")
    value = value.strip()
    if len(value) < low or len(value) > high: fail(f"{label} must contain {low}-{high} characters")
    return value

def main(path):
    project = json.loads(pathlib.Path("PROJECT.json").read_text())
    schema = json.loads(pathlib.Path("protocol/submission.schema.json").read_text())
    value = json.loads(pathlib.Path(path).read_text())
    allowed = {"schemaVersion","submissionId","projectId","objectiveId","base","workItemId","summary","method","finding","scope","uncertainty","failedSearches","recommendedAction","sources"}
    if not isinstance(value, dict) or set(value) != allowed: fail("top-level fields do not match schema")
    if type(value["schemaVersion"]) is not int or value["schemaVersion"] != 1: fail("unsupported schemaVersion")
    if not isinstance(value["submissionId"], str) or not UUID.fullmatch(value["submissionId"]): fail("submissionId must be a UUID")
    expected = pathlib.Path(path).name.removesuffix(".json")
    if pathlib.Path(path).parent.name == "submissions" and value["submissionId"].lower() != expected.lower(): fail("file name must equal submissionId")
    if value["projectId"] != project["projectId"] or value["objectiveId"] != project["objectiveId"]: fail("project identity mismatch")
    base = value["base"]
    if not isinstance(base, dict) or set(base) != {"revision","commit"}: fail("base fields do not match schema")
    if type(base["revision"]) is not int or base["revision"] < 0 or base["revision"] > project["acceptedRevision"]: fail("base revision is invalid")
    if not isinstance(base["commit"], str) or not re.fullmatch(r"[0-9a-fA-F]{40}", base["commit"]): fail("base commit must be a full Git SHA")
    for key, low, high in [("workItemId",1,160),("summary",20,280),("method",20,2000),("finding",20,8000),("scope",5,2000),("uncertainty",5,2000),("recommendedAction",5,2000)]: text(value[key], key, low, high)
    allowed_work = set(schema["properties"]["workItemId"].get("enum", []))
    if value["workItemId"] not in allowed_work: fail("workItemId must be an active research question")
    if not isinstance(value["failedSearches"], list) or len(value["failedSearches"]) > 20: fail("failedSearches must contain at most 20 strings")
    for item in value["failedSearches"]: text(item, "failed search", 1, 500)
    if not isinstance(value["sources"], list) or not 1 <= len(value["sources"]) <= 20: fail("sources must contain 1-20 records")
    kinds = {"vendor-doc","release-notes","benchmark","specification","reference-code","paper","blog","community-report"}
    source_fields = {"kind","title","url","documentDate","retrievedAt","exactExcerpt","relevance","contentHash"}
    for source in value["sources"]:
        if not isinstance(source, dict) or set(source) != source_fields: fail("source fields do not match schema")
        if source["kind"] not in kinds: fail("unsupported source kind")
        text(source["title"], "source title", 3, 300)
        parsed = urllib.parse.urlparse(text(source["url"], "source URL", 9, 2000))
        if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password: fail("source URL must be public HTTPS without embedded credentials")
        if source["documentDate"] is not None:
            if not isinstance(source["documentDate"], str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", source["documentDate"]): fail("documentDate must be a real YYYY-MM-DD date or null")
            try: datetime.date.fromisoformat(source["documentDate"])
            except Exception: fail("documentDate must be a real YYYY-MM-DD date or null")
        retrieved = text(source["retrievedAt"], "retrievedAt", 20, 40)
        if not TIMESTAMP.fullmatch(retrieved): fail("retrievedAt must be an ISO timestamp with a timezone")
        try: retrieved_time = datetime.datetime.fromisoformat(retrieved.replace("Z", "+00:00"))
        except Exception: fail("retrievedAt must be an ISO timestamp with a timezone")
        if retrieved_time.utcoffset() is None: fail("retrievedAt must be an ISO timestamp with a timezone")
        if retrieved_time > datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=5): fail("retrievedAt must not be in the future")
        text(source["exactExcerpt"], "exactExcerpt", 10, 4000)
        text(source["relevance"], "relevance", 10, 1000)
        if source["contentHash"] is not None and (not isinstance(source["contentHash"], str) or not re.fullmatch(r"[0-9a-fA-F]{64}", source["contentHash"])): fail("contentHash must be SHA-256 hex or null")
    print("OpenCat submission valid: " + value["submissionId"])

if __name__ == "__main__":
    if len(sys.argv) != 2: fail("usage: validate_submission.py submissions/<uuid>.json")
    main(sys.argv[1])
