import tweet_analysis.const as ta_const


def user_roles(request):
    return {'user_roles': ta_const.USER_ROLES}