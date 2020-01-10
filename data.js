const data = {
    "src/reducers/auth": {
        "ref": {
            "./data2/": [],
            "./data1/": []
        },
        "letter": "af"
    },
    "src/components/ListErrors": {
        "ref": {
            "./data2/": [],
            "./data1/": []
        },
        "letter": "h"
    },
    "src/agent": {
        "ref": {
            "./data2/": [],
            "./data1/": []
        },
        "letter": "e"
    },
    "src/components/Header": {
        "ref": {
            "./data2/": [],
            "./data1/": []
        },
        "letter": "k"
    },
    "src/components/Article/CommentList": {
        "ref": {
            "./data2/": ["src/components/Article/Comment"],
            "./data1/": ["src/components/Article/Comment"]
        },
        "letter": "ac"
    },
    "src/components/Article/ArticleActions": {
        "ref": {
            "./data2/": ["src/agent", "src/constants/actionTypes"],
            "./data1/": ["src/agent", "src/constants/actionTypes"]
        },
        "letter": "w"
    },
    "src/components/Register": {
        "ref": {
            "./data2/": ["src/components/ListErrors", "src/agent"],
            "./data1/": ["src/components/ListErrors", "src/agent"]
        },
        "letter": "j"
    },
    "src/components/Article/DeleteButton": {
        "ref": {
            "./data2/": ["src/agent", "src/constants/actionTypes"],
            "./data1/": ["src/agent", "src/constants/actionTypes"]
        },
        "letter": "ad"
    },
    "src/reducers/common": {
        "ref": {
            "./data2/": [],
            "./data1/": []
        },
        "letter": "aj"
    },
    "src/components/Login": {
        "ref": {
            "./data2/": ["src/components/ListErrors", "src/agent"],
            "./data1/": ["src/components/ListErrors", "src/agent"]
        },
        "letter": "m"
    },
    "src/components/ArticleList": {
        "ref": {
            "./data2/": ["src/components/ArticlePreview", "src/components/ListPagination"],
            "./data1/": ["src/components/ArticlePreview", "src/components/ListPagination"]
        },
        "letter": "o"
    },
    "src/components/Article/Comment": {
        "ref": {
            "./data2/": ["src/components/Article/DeleteButton"],
            "./data1/": ["src/components/Article/DeleteButton"]
        },
        "letter": "ab"
    },
    "src/components/ListPagination": {
        "ref": {
            "./data2/": ["src/agent", "src/constants/actionTypes"],
            "./data1/": ["src/agent", "src/constants/actionTypes"]
        },
        "letter": "r"
    },
    "src/components/ArticlePreview": {
        "ref": {
            "./data2/": ["src/agent", "src/constants/actionTypes"],
            "./data1/": ["src/agent", "src/constants/actionTypes"]
        },
        "letter": "l"
    },
    "src/components/Home/index": {
        "ref": {
            "./data2/": ["src/components/Home/Banner", "src/components/Home/MainView", "src/components/Home/Tags", "src/agent"],
            "./data1/": ["src/components/Home/Banner", "src/components/Home/MainView", "src/components/Home/Tags", "src/agent"]
        },
        "letter": "u"
    },
    "src/components/Editor": {
        "ref": {
            "./data2/": ["src/components/ListErrors", "src/agent"],
            "./data1/": ["src/components/ListErrors", "src/agent"]
        },
        "letter": "n"
    },
    "src/components/Article/CommentInput": {
        "ref": {
            "./data2/": ["src/agent", "src/constants/actionTypes"],
            "./data1/": ["src/agent", "src/constants/actionTypes"]
        },
        "letter": "z"
    },
    "src/components/Home/Banner": {
        "ref": {
            "./data2/": [],
            "./data1/": []
        },
        "letter": "v"
    },
    "src/components/Home/MainView": {
        "ref": {
            "./data2/": ["src/components/ArticleList", "src/agent", "src/constants/actionTypes"],
            "./data1/": ["src/components/ArticleList", "src/agent", "src/constants/actionTypes"]
        },
        "letter": "s"
    },
    "src/reducers/home": {
        "ref": {
            "./data2/": ["src/constants/actionTypes"],
            "./data1/": ["src/constants/actionTypes"]
        },
        "letter": "ag"
    },
    "src/components/Profile": {
        "ref": {
            "./data2/": ["src/components/ArticleList", "src/agent"],
            "./data1/": ["src/components/ArticleList", "src/agent"]
        },
        "letter": "g"
    },
    "src/components/Article/ArticleMeta": {
        "ref": {
            "./data2/": ["src/components/Article/ArticleActions"],
            "./data1/": ["src/components/Article/ArticleActions"]
        },
        "letter": "y"
    },
    "src/reducers/editor": {
        "ref": {
            "./data2/": [],
            "./data1/": []
        },
        "letter": "ah"
    },
    "src/components/ProfileFavorites": {
        "ref": {
            "./data2/": ["src/components/Profile", "src/agent"],
            "./data1/": ["src/components/Profile", "src/agent"]
        },
        "letter": "i"
    },
    "src/components/Settings": {
        "ref": {
            "./data2/": ["src/components/ListErrors", "src/agent"],
            "./data1/": ["src/components/ListErrors", "src/agent"]
        },
        "letter": "q"
    },
    "src/components/App": {
        "ref": {
            "./data2/": ["src/agent", "src/components/Header", "src/constants/actionTypes", "src/components/Editor", "src/components/Login", "src/components/Profile", "src/components/ProfileFavorites", "src/components/Register", "src/components/Settings", "src/store"],
            "./data1/": ["src/agent", "src/components/Header", "src/constants/actionTypes", "src/components/Editor", "src/components/Login", "src/components/Profile", "src/components/ProfileFavorites", "src/components/Register", "src/components/Settings", "src/store"]
        },
        "letter": "p"
    },
    "src/components/Home/Tags": {
        "ref": {
            "./data2/": ["src/agent"],
            "./data1/": ["src/agent"]
        },
        "letter": "t"
    },
    "src/reducer": {
        "ref": {
            "./data2/": ["src/reducers/article", "src/reducers/articleList", "src/reducers/auth", "src/reducers/common", "src/reducers/editor", "src/reducers/home", "src/reducers/profile", "src/reducers/settings"],
            "./data1/": ["src/reducers/article", "src/reducers/articleList", "src/reducers/auth", "src/reducers/common", "src/reducers/editor", "src/reducers/home", "src/reducers/profile", "src/reducers/settings"]
        },
        "letter": "a"
    },
    "src/store": {
        "ref": {
            "./data2/": ["src/middleware", "src/reducer"],
            "./data1/": ["src/middleware", "src/reducer"]
        },
        "letter": "b"
    },
    "src/components/Article/index": {
        "ref": {
            "./data2/": ["src/components/Article/ArticleMeta", "src/components/Article/CommentContainer", "src/agent", "src/constants/actionTypes"],
            "./data1/": ["src/components/Article/ArticleMeta", "src/components/Article/CommentContainer", "src/agent", "src/constants/actionTypes"]
        },
        "letter": "aa"
    },
    "src/reducers/article": {
        "ref": {
            "./data2/": [],
            "./data1/": []
        },
        "letter": "ai"
    },
    "src/constants/actionTypes": {
        "ref": {
            "./data2/": [],
            "./data1/": []
        },
        "letter": "f"
    },
    "src/components/Article/CommentContainer": {
        "ref": {
            "./data2/": ["src/components/Article/CommentInput", "src/components/Article/CommentList"],
            "./data1/": ["src/components/Article/CommentInput", "src/components/Article/CommentList"]
        },
        "letter": "x"
    },
    "src/reducers/articleList": {
        "ref": {
            "./data2/": [],
            "./data1/": []
        },
        "letter": "ak"
    },
    "src/middleware": {
        "ref": {
            "./data2/": ["src/agent"],
            "./data1/": ["src/agent"]
        },
        "letter": "d"
    },
    "src/index": {
        "ref": {
            "./data2/": ["src/store", "src/components/App"],
            "./data1/": ["src/store", "src/components/App"]
        },
        "letter": "c"
    },
    "src/reducers/profile": {
        "ref": {
            "./data2/": [],
            "./data1/": []
        },
        "letter": "ae"
    },
    "src/reducers/settings": {
        "ref": {
            "./data2/": [],
            "./data1/": []
        },
        "letter": "al"
    }
}