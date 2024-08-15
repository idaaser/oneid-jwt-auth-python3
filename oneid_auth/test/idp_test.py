# coding=utf-8
import oneid_auth

testLoginBaseURL = "https://oauth2.eid-6.account.tencentcs.com/v1/sso/jwtp/1102878596482998272/1151383032381308928/kit/{app_type}"
testIssuer = "https://www.example.com"
testPrivKey = """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDPwlvSsvsxHHKkRFeMvrBPvfGio2TLEHBCsoZ34KBmpjrJHLpcvVQ7K3SX3bRfplWH2qPs5EI9zt+LQ6Jlr1rMj7Nh/ZlX698rShdBtsfLX5rlFyFlJrQPOLnX1d9lD1i2FWFrCYe/CwHqx8+Y25KIgci1lyU7CgQXD944+Hkqv1pmYrqZJvl12fTR3gx2fiC/iAsFEBTpdSWavleE6i3vKPdfsp+Ojs9bHcv5btkPIBLGVMV2oRGjHxZdDwRQSaHo9DwnSSv6p+S+xcdALHRLMUNonQ1R9hDFRLRt7/G8fB+4+OrA4I5hmYZWOV9zi8CJ/S57miPLLHcrMEa8fWSnAgMBAAECggEACxTl4EY1tHfnptq9BL/Yba3G/r19DyvFoSPJR7ROj0sckETyV9ICyn6AjefVytL3dZ30PRrWbFo60usnoAmLa/qE6fF58BZKZWe399mvrH8L/F47JMcSDEx39TWY4INstZb3BvDk3GF87QX9YmeL2Ft71jEasPHRfV1rpVmeNOkUEaV1hLYsf3l9AZ7Im8hN+2Aarp0m7oMdOY3QVZ5bQ4qlbYsjPT3aCaZIpHoUCmUrKuyqNQDpXqXYZ6imBgaU9SzYHROJ+etAxyef8d/DbshrZ77OkI+xO1Nq8OClqfOBLeKnT4tr1S0t31mBWE1fFf1590UKmovZ2mm+zrXD8QKBgQDpU0g5fUcWBdsOeL+I6VZwB+iQcRIid0XiKI1bB4mdS+cA3JNFszy5y8jHY+2amVZ7Wvorl3ZICaGMLJncdChz4e2yJ5icAmLpJ7RVNnFm5oqM+EcXW5mLS99d7GlauY0ORUdDytdfv0aWqFwkltMNV7Z1VY4C+O0X2wsPwIK2DwKBgQDj8wmTSF/P4q4vhl5VFHK5HR5KaTxZ09myd82Xl1MTADjV3E3MBkDUWGhnRYFmwLCmnuXuMBTdA6nLHEpDnWW6Q1Xtbmt5k1x9D8B9nwbA2Tmz9hGvN1l8MlYPt2Hu+E17Je6kMCdy5Iz1QUevXc3cR0DLZwFGRhgXAyIS8cg/6QKBgQCuswrK8MA+/xdrmIFg08VCkMlTDTZU1BVhJpfgZp5lRiWqgX1LnM6FFs44bNvE+7bDGfVimj+X5I4u1F5HsDlxuuIsmHUtqqPAi1f8zYzPTSLENkmUdaNbpu2R96dSpMe2vayEV+Y27JK/z0NeqgdQYDJfXDW+h/+N8xYvLycvhQKBgDezFW3ly3OywjlergJAIuBU2yf3mwWgHJvdZmFaWrRT449ua5wlEwZQLALAGySOhRvRzAFtwktXL9Avs33eIhNnjMGdr6lfdsQgazrG9xF8gvsUb7HO5pDQg/MHLmkER3qGBFAebCVI76CmOOwDEeB3kL+jBc60JgLJgzP53KKxAoGBANKZ9xIWiSyRICUIHwpWClizXj9dyXaHOl6INqd/Jj+1dqdizI7YoVufm6vDP0vKf467HKLwLm5mDlZr3j+j/Y/WkbZqluT8onPx4F7m5f8dJUu/OJtGBc1+OnfzyFt5xSAD0Q6NDAxDdKuKCV36znRdNbZu/WiICncDQIjaNCeQ
-----END PRIVATE KEY-----"""


def _test_new_jwt_config():
    jwt_config = oneid_auth.JwtConfig(testPrivKey, testIssuer, testLoginBaseURL)
    print(jwt_config.as_claims())
    return jwt_config


def _test_generate_token_with_user_info():
    jwt_config = _test_new_jwt_config()
    token = oneid_auth.generate_token(jwt_config, user_info=oneid_auth.UserInfo("user_id_123", name="jinrruan",
                                                                                email="jinrruan@qq.com"))
    print(token)


def _test_generate_token_with_claims():
    jwt_config = _test_new_jwt_config()
    token = oneid_auth.generate_token(jwt_config,
                                      claims={"user_id": "user_id_123", "name": "jinrruan", "email": "jinrruan@qq.com",
                                              "haha": "====", "iss": "jinrruan"})
    print(token)


def _test_generate_login_url_with_user_info():
    jwt_config = _test_new_jwt_config()
    cur_user_info = oneid_auth.UserInfo("user_id_123", name="jinrruan", email="jinrruan@qq.com")
    login_url = oneid_auth.generate_login_url(jwt_config,
                                              user_info=cur_user_info,
                                              app=oneid_auth.App_Tencent_Meeting,
                                              params={"name": "1+2", "age": 18, "email": "123@qq.com"})
    print(login_url)


def _test_generate_login_url_with_claims():
    jwt_config = _test_new_jwt_config()
    cur_claims = {"user_id": "user_id_123", "name": "jinrruan",
                  "email": "jinrruan@qq.com",
                  "haha": "====", "iss": "jinrruan"}
    login_url = oneid_auth.generate_login_url(jwt_config,
                                              claims=cur_claims,
                                              app=oneid_auth.App_Tencent_Docs,
                                              params={"name": "1+2", "age": 18, "email": "123@qq.com"})
    print(login_url)


if __name__ == '__main__':
    _test_generate_token_with_claims()
