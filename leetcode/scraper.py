import requests
import sys

from leetcode.db import save_stat, user_to_platform_uname

platform = 'leetcode'
base_url = 'https://leetcode.com'

query_url = 'https://leetcode.com/graphql'


def initialize():
    payload = {
        "query": """
        {
            allQuestionsCount {
                difficulty
                count
            }
        }
        """
    }

    response = requests.post(
        url = query_url,
        json = payload,
        headers = {
            'referer': base_url
        }
    )

    assert( response.status_code == 200 )
    return response.json()




def questions_solved_count(username: str):
    payload = {
            "variables": {
                "username": username
            },
            "query": """
            query getUserProfile($username: String!) {
                matchedUser(username: $username) {
                    submitStats {
                        acSubmissionNum {
                            difficulty
                            count
                            submissions
                        }
                    }
                }
            }
            """
        }


    response = requests.post(
        url = query_url, 
        json = payload,
        headers = {
            'referer': base_url + '/' + username,
        },
    )

    assert( response.status_code == 200 )

    response_data = response.json()
    if 'errors' in response_data:
        print(response_data['errors'], file=sys.stderr)
        return dict()

    submission_stats = response_data['data']['matchedUser']['submitStats']['acSubmissionNum']

    save_stat(username, {'submission': submission_stats})

    return submission_stats


def contributions(username: str):
    payload = {
            "variables": {
                "username": username
            },
            "query": """ 
            query getUserProfile($username: String!) {
                matchedUser(username: $username) {
                    contributions {
                        points
                        questionCount
                        testcaseCount
                    }
                }
            }
            """
        }

    response = requests.post(
        url = query_url,
        json = payload,
        headers = {
            'referer': base_url + '/' + username
        }
    )

    assert( response.status_code == 200 )

    response_data = response.json()
    if 'errors' in response_data:
        print(response_data['errors'], file=sys.stderr)
        return dict()

    contribution_stats = response_data['data']['matchedUser']['contributions']

    save_stat(username, {'contribution': contribution_stats})
    
    return contribution_stats

def profile(username: str):
    payload = {
            "variables": {
                "username": username
            },
            "query": """ 
            query getUserProfile($username: String!) {
                matchedUser(username: $username) {
                    profile {
                        reputation
                        ranking
                    }
                }
            }
            """
        }

    response = requests.post(
        url = query_url,
        json = payload,
        headers = {
            'referer': base_url + '/' + username
        }
    )

    assert( response.status_code == 200 )

    response_data = response.json()
    if 'errors' in response_data:
        print(response_data['errors'], file=sys.stderr)
        return dict()

    profile_stat = response_data['data']['matchedUser']['profile']

    save_stat(username, {'profile': profile_stat})

    return profile_stat


def total_submissions(username: str):
    payload = {
            "variables": {
                "username": username
            },
            "query": """ 
            query getUserProfile($username: String!) {
                matchedUser(username: $username) {
                    submitStats {
                        totalSubmissionNum {
                            difficulty
                            count
                            submissions
                        }
                    }
                }
            }
            """
        }

    response = requests.post(
        url = query_url,
        json = payload,
        headers = {
            'referer': base_url + '/' + username
        }
    )

    assert( response.status_code == 200 )

    response_data = response.json()
    if 'errors' in response_data:
        print(response_data['errors'], file=sys.stderr)
        return dict()

    total_submissions_stat = response_data['data']['matchedUser']['submitStats']['totalSubmissionNum']

    save_stat(username, {'total_submission': total_submissions_stat})

    return total_submissions_stat




def search_question_by_name(question_name: str, skip : int = 0, limit : int = 50):
    payload = {
            "variables": {
                "categorySlug": "",
                "limit": limit,
                "skip": skip,
                "filters": {
                    "searchKeywords": question_name,
                }
            },
            "query": """ 
                query problemsetQuestionList(
                    $categorySlug: String
                    $limit: Int
                    $skip: Int
                    $filters: QuestionListFilterInput
                ) {
                    problemsetQuestionList: questionList(
                    categorySlug: $categorySlug
                    limit: $limit
                    skip: $skip
                    filters: $filters
                    ) {
                        total: totalNum
                        questions: data {
                        difficulty
                        title
                    }
                }
            }
            """
        }

    response = requests.post(
        url = query_url,
        json = payload,
        headers = {
            'referer': base_url + '/problemset/all'
        }
    )

    assert( response.status_code == 200 )

    response_data = response.json()
    if 'errors' in response_data:
        print(response_data['errors'], file=sys.stderr)
        return dict()

    submission_stats = response_data['data']['problemsetQuestionList']
    return submission_stats


def scrap_now(user):
    p_uname = user_to_platform_uname(user)
    print(p_uname)
    if not p_uname:
        return {}
    
    details = {
        'submission': questions_solved_count(p_uname),
        'contribution': contributions(p_uname),
        'profile': profile(p_uname),
        'total_submission': total_submissions(p_uname),
    }

    save_stat(user, details)

    return details