import os
import logging
from typing import Any, Dict, List

try:
	import joblib
except Exception:
	joblib = None

MODEL_PATH = os.path.join(os.path.dirname(__file__), "at_risk_model.pkl")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def load_model():
	if not joblib:
		logger.warning("joblib not available; can't load model")
		return None
	if not os.path.exists(MODEL_PATH):
		logger.warning(f"Model file not found at {MODEL_PATH}")
		return None
	try:
		model = joblib.load(MODEL_PATH)
		logger.info("Model loaded successfully")
		return model
	except Exception as e:
		logger.exception("Failed to load model: %s", e)
		return None

_MODEL = load_model()

def predict(features: List[float]) -> Dict[str, Any]:
	if _MODEL is None:
		logger.info("No model available; returning dummy prediction")
		return {"prediction": 0, "probability": 0.0, "note": "model-missing"}

	import numpy as _np

	try:
		arr = _np.array(features, dtype=float)
		if arr.ndim == 1:
			arr = arr.reshape(1, -1)
		pred = _MODEL.predict(arr)
		result: Dict[str, Any] = {}
		result["prediction"] = int(pred[0])
		if hasattr(_MODEL, "predict_proba"):
			proba = _MODEL.predict_proba(arr)
			result["probability"] = float(proba[0][1]) if proba.shape[1] > 1 else float(proba[0][0])
		return result
	except Exception as e:
		logger.exception("Prediction failed: %s", e)
		return {"prediction": None, "error": str(e)}

