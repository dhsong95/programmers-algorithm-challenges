import re


def transform_page(page, tag):
    tag_start = '<' + tag + '>'
    start = page.find(tag_start) + len(tag_start)

    tag_end = '</' + tag + '>'
    end = page.find(tag_end)

    return page[start:end]


def solution(word, pages):
    word = word.lower()
    page_head = list()
    page_body = list()
    for page in pages:
        page = page.lower()
        page_head.append(transform_page(page, 'head'))
        page_body.append(transform_page(page, 'body'))

    links = list()
    for page in page_head:
        # difference between .*(greedy) and .*?(non greedy)
        link = re.search(r'<meta.*?\"(https://.*?)\"', page).group(1)
        links.append(link)

    base_scores = list()
    outer_links = list()
    for page in page_body:
        base_score = re.sub(r'[^a-z]', '.', page).split('.').count(word)
        base_scores.append(base_score)

        outer_link = re.findall(r'<a href=\"(https://.*?)\"', page)
        outer_links.append(outer_link)

    N = len(pages)
    scores = list()
    for idx in range(N):
        score = base_scores[idx]
        link = links[idx]
        for jdx in range(N):
            if idx == jdx:
                continue
            outer_link = outer_links[jdx]
            if link in outer_link:
                score += base_scores[jdx] / len(outer_link)
        scores.append(score)

    score_max = max(scores)
    return scores.index(score_max)


if __name__ == "__main__":
    word = 'blind'
    pages = ["""<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>""", """<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>""", """<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"""]
    solution(word, pages) == 0

    word = 'Muzi'
    pages = ["""<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>""", """<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"""]
    solution(word, pages) == 1
