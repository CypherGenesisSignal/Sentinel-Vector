TEST_INPUT = {
    "surface": {
        "services": ["http", "ssh", "metrics"],
        "configs": {"valid": True}
    },
    "target": "10.0.0.45"
}

EXPECTED_ORDERING = [1, 2, 3]
