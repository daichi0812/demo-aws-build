from src.app import lambda_handler

def test_lambda_handler():
    res = lambda_handler({}, None)
    assert res["statusCode"] == 200