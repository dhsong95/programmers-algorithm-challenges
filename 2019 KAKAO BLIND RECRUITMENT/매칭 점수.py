import re


def solution(word, pages):
    word = word.lower()
    links = list()
    outer_links = list()
    base_scores = list()
    for page in pages:
        page = page.lower()

        head_start = page.index('<head>') + len('<head>')
        head_last = page.index('</head>')
        page_head = page[head_start:head_last]

        body_start = page.index('<body>') + len('<body>')
        body_last = page.index('</body>')
        page_body = page[body_start:body_last]

        link = re.search(
            r'<meta property=\"og:url\" ?content=\"(https://.+?)\"/>',
            page_head
        ).group(1)
        links.append(link)

        outer_link = re.findall(r'<a href=\"(https://.+?)\"', page_body)
        outer_links.append(outer_link)

        base_score = re.sub(r'[^a-z]+', '.', page_body).split('.').count(word)
        base_scores.append(base_score)

    scores = list()
    for idx in range(len(pages)):
        score = base_scores[idx]
        link = links[idx]

        for jdx in range(len(pages)):
            if idx == jdx:
                continue

            outer_link = outer_links[jdx]
            if link in outer_link:
                link_score = base_scores[jdx] / len(outer_link)
                score += link_score

        scores.append(score)

    score_max = max(scores)
    return scores.index(score_max)


if __name__ == "__main__":
    word = 'blind'
    pages = ["""<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>""", """<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>""", """<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"""]
    solution(word, pages)

    word = 'Muzi'
    pages = ["""<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>""", """<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"""]
    solution(word, pages)
