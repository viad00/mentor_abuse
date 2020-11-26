ANSWERS = {
    535: {
        "StudentId": None,
        "AccessToken": None,
        "TopicId": 535,
        "TestIds": [
            2689,
            2695,
            5659
        ],
        "Answers": [
            1,
            2,
            1
        ],
        "StartTestDT": "2020-09-15 12:14:42",
        "FinishTestDT": "2020-09-15 12:16:16",
        "Rating": 0,
        "ErrorCount": 0,
        "Year": 2020,
        "Sem": 1
    },
    393: {
        "StudentId": None,
        "AccessToken": None,
        "TopicId": 393,
        "TestIds": [
            2689,
            2695,
            5659
        ],
        "Answers": [
            1,
            2,
            1
        ],
        "StartTestDT": "2020-09-22 12:15:11",
        "FinishTestDT": "2020-09-22 12:19:07",
        "Rating": "5",
        "ErrorCount": 0,
        "Year": 2020,
        "Sem": 1
    },
    398: {
        "StudentId": None,
        "AccessToken": None,
        "TopicId": 398,
        "TestIds": [
            2741,
            5675,
            5677
        ],
        "Answers": [
            3,
            3,
            1
        ],
        "StartTestDT": "2020-09-29 12:09:10",
        "FinishTestDT": "2020-09-29 12:11:56",
        "Rating": 0,
        "ErrorCount": 0,
        "Year": 2020,
        "Sem": 1
    },
    408: {
        "StudentId": None,
        "AccessToken": None,
        "TopicId": 408,
        "TestIds": [
            2741,
            5675,
            5677
        ],
        "Answers": [
            3,
            3,
            1
        ],
        "StartTestDT": "2020-10-13 12:09:28",
        "FinishTestDT": "2020-10-13 12:11:42",
        "Rating": 0,
        "ErrorCount": 0,
        "Year": 2020,
        "Sem": 1
    },
    508: {
        "StudentId": None,
        "AccessToken": None,
        "TopicId": 508,
        "TestIds": [
            2741,
            5675,
            5677
        ],
        "Answers": [
            3,
            3,
            1
        ],
        "StartTestDT": "2020-10-20 14:48:52",
        "FinishTestDT": "2020-10-20 14:52:43",
        "Rating": 0,
        "ErrorCount": 0,
        "Year": 2020,
        "Sem": 1
    },
    609: {
        "StudentId": None,
        "AccessToken": None,
        "TopicId": 609,
        "TestIds": [
            2741,
            5675,
            5677
        ],
        "Answers": [
            3,
            3,
            1
        ],
        "StartTestDT": "2020-10-27 14:59:21",
        "FinishTestDT": "2020-10-27 15:01:41",
        "Rating": 0,
        "ErrorCount": 0,
        "Year": 2020,
        "Sem": 1
    },
    418: {
        "StudentId": None,
        "AccessToken": None,
        "TopicId": 418,
        "TestIds": [
            2741,
            5675,
            5677
        ],
        "Answers": [
            3,
            3,
            1
        ],
        "StartTestDT": "2020-11-10 14:55:36",
        "FinishTestDT": "2020-11-10 14:58:44",
        "Rating": 0,
        "ErrorCount": 0,
        "Year": 2020,
        "Sem": 1
    },
    550: {
        "StudentId": None,
        "AccessToken": None,
        "TopicId": 550,
        "TestIds": [
            2741,
            5675,
            5677
        ],
        "Answers": [
            3,
            3,
            1
        ],
        "StartTestDT": "2020-11-18 14:55:15",
        "FinishTestDT": "2020-11-18 14:59:34",
        "Rating": 0,
        "ErrorCount": 0,
        "Year": 2020,
        "Sem": 1
    },
    424: {
        "StudentId": None,
        "AccessToken": None,
        "TopicId": 424,
        "TestIds": [
            2741,
            5675,
            5677
        ],
        "Answers": [
            3,
            3,
            1
        ],
        "StartTestDT": "2020-11-24 20:35:21",
        "FinishTestDT": "2020-11-24 20:36:41",
        "Rating": 0,
        "ErrorCount": 0,
        "Year": 2020,
        "Sem": 1
    }
}

import random


def generate_test(test,id,token):
    ans = ANSWERS[test]
    ans["StudentId"] = id
    ans["AccessToken"] = token
    ans["StartTestDT"] = ans["StartTestDT"][:-1]+str(random.randint(0,9))
    ans["FinishTestDT"] = ans["FinishTestDT"][:-1] + str(random.randint(0,9))
    return ans


if __name__ == '__main__':
    print(ANSWERS)
    print(generate_test(test=424,id="0", token="test"))
