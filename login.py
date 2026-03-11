def login(username, password):
    """用户登录功能"""
    if username and password:
        return "登录成功"
    return "登录失败"