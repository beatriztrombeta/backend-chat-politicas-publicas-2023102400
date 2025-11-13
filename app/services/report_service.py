import os
import jwt
import time
from dotenv import load_dotenv
from app.data.reports_list import REPORTS_MAP  # importa o mapa

load_dotenv()

METABASE_SITE_URL = os.getenv("METABASE_SITE_URL")
METABASE_SECRET_KEY = os.getenv("METABASE_SECRET_KEY")


def generate_metabase_link(question_id: int) -> str:
    dashboard_id = REPORTS_MAP.get(question_id)
    if not dashboard_id:
        return None

    payload = {
        "resource": {"dashboard": dashboard_id},
        "params": {},
        "exp": round(time.time()) + (60 * 10),
    }

    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
    iframe_url = f"{METABASE_SITE_URL}/embed/dashboard/{token}#bordered=true&titled=true"
    return iframe_url
