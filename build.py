# -*- coding: utf-8 -*-
"""오피스워크넷 고덕강일점 정적 사이트 생성기 (GitHub Pages용)
python3 build.py  →  docs/ 폴더에 HTML 생성
"""
import os, datetime, html
from urllib.parse import quote

SITE_URL = "https://officeworknet-gangil.kr"   # 배포 후 실제 주소로 교체
BRAND = "오피스워크넷 고덕강일점"
ADDR = "서울 강동구 아리수로93길 33-9 강일프라자 5층 501호"
MAP = "https://map.naver.com/p/search/%EC%98%A4%ED%94%BC%EC%8A%A4%EC%9B%8C%ED%81%AC%EB%84%B7%20%EA%B3%A0%EB%8D%95%EA%B0%95%EC%9D%BC%EC%A0%90"                 # 번지·건물명 확인 필요
TALK = "https://talk.naver.com/ct/wnhe5hg"                                 # 네이버 톡톡 링크로 교체
NAVER_VERIFY = "9036c369de6061e721796b0d380158464fa435b9"                                                # 서치어드바이저 메타 내용 넣기
TODAY = datetime.date.today().isoformat()
OUT = "docs"

NAV = [("index.html","홈"),("virtual-office.html","비상주 사무실"),("private-office.html","상주 사무실"),
       ("lounge.html","라운지 고정석"),("pricing.html","요금 안내"),("location.html","오시는 길"),("blog/index.html","오피스 소식")]

def layout(title, desc, body, path, canonical, active="", jsonld=""):
    depth = path.count("/")
    rel = "../"*depth
    nav = "".join('<li><a href="%s%s"%s>%s</a></li>' % (rel, h, ' class="active"' if h==active else '', t) for h,t in NAV)
    verify = f'<meta name="naver-site-verification" content="{NAVER_VERIFY}">' if NAVER_VERIFY else ""
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:image" content="{SITE_URL}/img/entrance.jpg">
<meta name="robots" content="index,follow">
{verify}
<link rel="alternate" type="application/rss+xml" title="{BRAND} 오피스 소식" href="{SITE_URL}/rss.xml">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<link rel="stylesheet" href="{rel}style.css">
{jsonld}
</head>
<body>
<div class="topbar"><div class="wrap"><span>{BRAND} · 서울 강동구 강일동 · 강일역 인근</span><span>문의는 네이버 톡톡으로</span></div></div>
<header class="site"><div class="wrap">
  <a class="logo" href="{rel}index.html"><i></i>오피스워크넷 <span>고덕강일점</span></a>
  <button class="nav-toggle" onclick="document.querySelector('nav.main').classList.toggle('open')">메뉴</button>
  <nav class="main"><ul>{nav}</ul></nav>
</div></header>
{body}
<footer class="site"><div class="wrap">
  <div><strong>{BRAND}</strong>{ADDR}<br>대표 박미애<br>문의: 네이버 톡톡</div>
  <div><strong>서비스</strong><ul><li><a href="{rel}virtual-office.html">비상주 사무실</a></li><li><a href="{rel}private-office.html">상주 사무실</a></li><li><a href="{rel}lounge.html">라운지 고정석</a></li><li><a href="{rel}pricing.html">요금 안내</a></li></ul></div>
  <div><strong>안내</strong><ul><li><a href="{rel}location.html">오시는 길</a></li><li><a href="{rel}blog/index.html">오피스 소식</a></li><li><a href="https://officeworknet.co.kr/" target="_blank" rel="noopener">오피스워크넷 전국 지점</a></li></ul></div>
  <div class="copy">© {datetime.date.today().year} {BRAND}. 모든 요금은 부가세 별도입니다.</div>
</div></footer>
<a class="fab" href="{TALK}" target="_blank" rel="noopener">톡톡 문의</a>
</body></html>"""

def cta(title="질문 하나만 보내주세요", text="어떤 상품이 맞는지, 지금 빈 방이 있는지, 우리 업종도 가능한지 — 톡톡으로 물어보시면 운영자가 직접 답합니다. 영업 전화는 하지 않습니다."):
    return f'<section class="cta"><h2>{title}</h2><p>{text}</p><a class="btn btn-primary" href="{TALK}" target="_blank" rel="noopener">네이버 톡톡으로 묻기</a></section>'

FAQ = [
 ("비상주 사무실 주소로 사업자등록이 되나요?","임대차계약서를 받아 홈택스나 세무서에서 진행합니다. 음식점처럼 실제 영업장이 필요한 업종은 안 되므로 톡톡으로 업종을 먼저 확인해 드립니다."),
 ("계약하러 직접 가야 하나요?","비상주는 온라인으로 끝납니다. 상주·라운지는 방문 후 계약을 권합니다."),
 ("우편물이 오면 어떻게 되나요?","도착하면 알림을 보내드립니다. 방문 수령 또는 사진 전달이 가능합니다."),
 ("주차는 되나요?","본 건물에는 주차가 불가합니다. 차로 오시면 건물 주변 공영주차장 2곳을 유료로 이용해 주세요. 강일동 공영주차장은 5분당 150원, 강일동 노상주차장은 5분당 250원(시간제)이며, 경차·전기차 등은 강동구 조례에 따라 할인됩니다. 이름이 비슷하니 이용 전 주차장명을 꼭 확인하세요."),
 ("주말에도 사무실을 쓸 수 있나요?","24시간 출입 시스템으로 주말·공휴일도 이용합니다."),
 ("중간에 다른 상품으로 바꿀 수 있나요?","비상주에서 라운지, 라운지에서 상주로 옮길 수 있습니다. 남은 기간은 정산해 드립니다."),
 ("법인도 계약할 수 있나요?","네. 법인은 비상주 월 3만원부터이고, 등기부등본이 필요합니다."),
 ("세금계산서 발행되나요?","네, 모든 요금에 세금계산서를 발행합니다."),
]
def faq_html(items=FAQ):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in items) + "</div>"
def faq_jsonld(items=FAQ):
    import json
    d={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in items]}
    return f'<script type="application/ld+json">{json.dumps(d,ensure_ascii=False)}</script>'

BIZ_JSONLD = f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"LocalBusiness","name":"{BRAND}","address":{{"@type":"PostalAddress","streetAddress":"아리수로93길 33-9 강일프라자 5층 501호","addressLocality":"강동구","addressRegion":"서울","addressCountry":"KR"}},"url":"{SITE_URL}/","priceRange":"₩20,000~₩460,000","openingHours":"Mo-Su 00:00-24:00","parentOrganization":{{"@type":"Organization","name":"오피스워크넷","url":"https://officeworknet.co.kr/"}}}}</script>'''

PRIVATE_TABLE = """<table><thead><tr><th>타입</th><th>위치</th><th class="num">월 요금(부가세 별도)</th><th>이런 분께</th></tr></thead><tbody>
<tr><td>1인실 내측</td><td>창 없는 조용한 자리</td><td class="num">270,000원</td><td>통화·집중 작업이 많은 1인 사업자</td></tr>
<tr><td>1인실 창측</td><td>창 있음, 채광 좋음</td><td class="num">350,000원</td><td>하루 종일 있어도 답답하지 않은 자리를 원하는 분</td></tr>
<tr><td>2인실 내측</td><td>책상 2개</td><td class="num">400,000원</td><td>동업자 2인, 직원 1명 채용 직후</td></tr>
<tr><td>2인실 창측</td><td>책상 2개, 창 있음</td><td class="num">460,000원</td><td>여유 있는 2인 공간</td></tr>
</tbody></table><p class="note">6개월 결제 시 6만원 할인, 1년 결제 시 1개월 추가 이용.</p>"""
LOUNGE_TABLE = """<table><thead><tr><th>좌석</th><th class="num">월 요금(부가세 별도)</th><th>특징</th></tr></thead><tbody>
<tr><td>라운지석</td><td class="num">100,000원</td><td>개방형, 가장 경제적</td></tr>
<tr><td>창가석</td><td class="num">120,000원</td><td>창 옆, 채광 좋음</td></tr>
<tr><td>프리미엄석</td><td class="num">150,000원</td><td>넓은 책상, 가림 있음</td></tr>
</tbody></table><p class="note">6개월 결제 시 6만원 할인, 1년 결제 시 1개월 추가 이용.</p>"""
VIRTUAL_TABLE = """<table><thead><tr><th>계약 기간</th><th class="num">개인사업자 월</th><th class="num">법인 월</th><th class="num">계약 시 총액(개인, VAT 포함)</th></tr></thead><tbody>
<tr><td>1년</td><td class="num">20,000원</td><td class="num">30,000원</td><td class="num">264,000원</td></tr>
<tr><td>6개월</td><td class="num">30,000원</td><td class="num">40,000원</td><td class="num">198,000원</td></tr>
<tr><td>3개월</td><td class="num">40,000원</td><td class="num">50,000원</td><td class="num">132,000원</td></tr>
</tbody></table><p class="note">3년 장기 계약은 법인도 개인 1년 요금으로 계약합니다.</p>"""

pages = {}

# ---------- 홈 ----------
pages["index.html"] = dict(
 title="오피스워크넷 고덕강일점 | 강일동 공유오피스·1인사무실·비상주사무실",
 desc="강일동 공유오피스. 비상주 월 2만원, 라운지 고정석 월 10만원, 1인실 월 27만원부터. 강일리버파크·고덕·미사 인근, 강일역 도보권.",
 active="index.html", jsonld=BIZ_JSONLD,
 body=f"""
<section class="hero"><div class="wrap hero-grid">
  <div>
  <h1>사무실은 필요한데,<br>임대료는 부담되는 분께</h1>
  <p class="lead">서울 강동구 강일동, 강일역 인근 공유오피스. 사업자등록용 주소는 월 2만원부터, 내 책상 하나는 월 10만원부터, 독립된 1인실은 월 27만원부터 시작합니다. (부가세 별도)</p>
  <div class="btn-row"><a class="btn btn-primary" href="{TALK}" target="_blank" rel="noopener">네이버 톡톡으로 1분 상담</a><a class="btn btn-outline" href="pricing.html">요금표 보기</a></div>
  </div>
  <img class="hero-img" src="img/entrance.jpg" alt="오피스워크넷 고덕강일점 입구와 라운지" width="1600" height="1200">
</div></section>
<section><div class="wrap">
  <h2>세 가지 중 하나만 고르면 됩니다</h2>
  <p class="sub">필요한 만큼만 계약합니다. 모두 부가세 별도입니다.</p>
  <div class="cards">
    <div class="card"><h3>비상주 사무실</h3><div class="price">월 20,000원~ <small>1년 계약, 개인</small></div><p>사업자등록·법인설립용 주소만 필요한 분. 온라인으로 계약하고 방문 없이 시작합니다.</p><a class="btn btn-outline" href="virtual-office.html">자세히 보기</a></div>
    <div class="card"><h3>라운지 고정석</h3><div class="price">월 100,000원~</div><p>카페는 집중이 안 되고, 사무실은 과한 분. 내 자리가 정해진 책상 하나.</p><a class="btn btn-outline" href="lounge.html">자세히 보기</a></div>
    <div class="card"><h3>상주 사무실</h3><div class="price">월 270,000원~</div><p>문 닫히는 내 공간이 필요한 1~2인 사업자. 책상·의자·인터넷이 준비된 상태로 입주 당일부터 일합니다.</p><a class="btn btn-outline" href="private-office.html">자세히 보기</a></div>
  </div>
</div></section>
<section class="alt"><div class="wrap">
  <h2>공간 둘러보기</h2>
  <p class="sub">사진은 모두 실제 촬영본입니다.</p>
  <div class="gallery">
    <figure><img src="img/room-1p-a.jpg" alt="강일동 1인 사무실 창측" loading="lazy"><figcaption>1인실 창측</figcaption></figure>
    <figure><img src="img/room-2p.jpg" alt="강일동 2인 사무실" loading="lazy"><figcaption>2인실</figcaption></figure>
    <figure><img src="img/lounge.jpg" alt="라운지 고정석" loading="lazy"><figcaption>라운지</figcaption></figure>
    <figure><img src="img/meeting-room.jpg" alt="미팅룸" loading="lazy"><figcaption>미팅룸</figcaption></figure>
  </div>
</div></section>
<section><div class="wrap">
  <h2>왜 고덕강일점인가</h2>
  <div class="points">
    <div><strong>필요한 만큼만 계약</strong><p>비상주는 3개월부터, 라운지와 사무실은 월 단위로 시작합니다. 6개월 결제 시 6만원 할인, 1년 결제 시 1개월을 더 드립니다.</p></div>
    <div><strong>운영자가 같은 건물에 있습니다</strong><p>우편물, 계약 변경, 작은 불편 모두 당일 답변합니다. 관리 회사가 아니라 운영자가 직접 답합니다.</p></div>
    <div><strong>전국 지점을 운영하는 오피스워크넷 시스템</strong><p>계약·결제·우편물 알림이 시스템으로 처리됩니다. 24시간 출입으로 주말·야간 작업이 가능합니다.</p></div>
  </div>
</div></section>
<section class="alt"><div class="wrap">
  <h2>이런 분들이 사용 중입니다</h2>
  <div class="tags"><span>온라인 쇼핑몰·스마트스토어</span><span>프리랜서 디자이너·개발자</span><span>방문 수업·방문 서비스</span><span>재택근무에서 분리가 필요한 분</span><span>법인 설립 준비 중인 예비창업자</span><span>강일리버파크·미사·고덕 거주 사업자</span></div>
</div></section>
<section><div class="wrap">
  <h2>자주 묻는 질문</h2>
  {faq_html()}
</div></section>
<section class="alt"><div class="wrap">
  <h2>오시는 길</h2>
  <p>{ADDR}</p>
  <div class="btn-row"><a class="btn btn-primary" href="{MAP}" target="_blank" rel="noopener">네이버 지도에서 보기</a><a class="btn btn-outline" href="location.html">시설·주차 안내</a></div>
</div></section>
{cta()}
""" + faq_jsonld())

# ---------- 비상주 ----------
pages["virtual-office.html"] = dict(
 title="비상주사무실 월 2만원부터 | 사업자등록 주소 임대 오피스워크넷 고덕강일점",
 desc="강동구 비상주 사무실. 사업자등록·법인설립 주소 월 2만원부터. 온라인 계약, 우편물 도착 알림, 세금계산서 발행.",
 active="virtual-office.html",
 body=f"""
<div class="wrap"><p class="breadcrumb">홈 › 비상주 사무실</p></div>
<div class="page-head wrap"><h1>비상주 사무실 — 사업자등록 주소, 월 2만원부터</h1>
<p class="lead">집 주소로 사업자등록을 하면 집 주소가 쇼핑몰·세금계산서·명함에 그대로 노출됩니다. 오피스워크넷 고덕강일점 비상주 사무실은 서울 강동구의 실제 사무실 주소를 사업자등록과 법인설립에 쓰도록 임대합니다. 방문 없이 온라인으로 계약하고 임대차계약서를 받습니다.</p></div>
<section><div class="wrap">
  <h2>요금 (부가세 별도)</h2>{VIRTUAL_TABLE}
</div></section>
<section class="alt"><div class="wrap">
  <h2>이렇게 쓸 수 있습니다</h2>
  <ul class="compare"><li>개인사업자 사업자등록 주소 (통신판매업 신고 포함)</li><li>법인 설립 등기용 본점 주소</li><li>우편물·등기우편 수령 후 도착 알림</li><li>사업자등록증·명함·쇼핑몰 사업자 정보 표기</li></ul>
</div></section>
<section><div class="wrap">
  <h2>계약까지 3단계</h2>
  <div class="steps">
    <div><strong>톡톡으로 알려주세요</strong><p>개인/법인 여부와 계약 기간만 남겨주시면 됩니다.</p></div>
    <div><strong>서류와 입금</strong><p>신분증 사본(법인은 등기부등본)을 보내고 입금합니다.</p></div>
    <div><strong>계약서 수령</strong><p>임대차계약서를 받아 홈택스에서 사업자등록을 진행합니다.</p></div>
  </div>
</div></section>
<section class="alt"><div class="wrap">
  <h2>많이 묻는 질문</h2>
  {faq_html(FAQ[:1]+[("중간에 해지하면 환불되나요?","계약서 기준으로 안내합니다. 계약 전에 해지 조건을 먼저 설명해 드립니다."),("필요할 때 사무실을 쓸 수 있나요?","라운지 고정석이나 상주 사무실로 전환할 수 있습니다. 남은 기간은 정산합니다.")])}
</div></section>
{cta("오늘 계약하면 오늘 사업자등록 신청까지","톡톡으로 계약 기간만 남겨주세요. 개인/법인 구분과 업종만 확인하고 바로 진행합니다.")}
""")

# ---------- 상주 ----------
pages["private-office.html"] = dict(
 title="강일동 1인사무실·2인사무실 월 27만원부터 | 강일리버파크·고덕·미사 공유오피스",
 desc="강일동 공유오피스 상주 사무실. 문 닫히는 1인실·2인실 월 27만원부터, 책상·의자·인터넷 포함. 강일역 인근.",
 active="private-office.html",
 body=f"""
<div class="wrap"><p class="breadcrumb">홈 › 상주 사무실</p></div>
<div class="page-head wrap"><h1>강일동 1인 사무실·2인 사무실 — 월 27만원부터</h1>
<p class="lead">강일리버파크·고덕·미사에서 집 근처 사무실을 찾으면 보통 두 가지에 막힙니다. 상가 사무실은 보증금과 관리비가 붙고, 카페는 전화 한 통 마음 편히 못 받습니다. 오피스워크넷 고덕강일점은 강일역 인근에 문 닫히는 1인실·2인실을 월 요금 하나로 운영합니다. 관리비·인터넷·냉난방 모두 포함입니다.</p></div>
<section><div class="wrap">
  <div class="gallery three">
    <figure><img src="img/room-1p-a.jpg" alt="1인실 창측 — 창밖으로 강일동 전경" loading="lazy"><figcaption>1인실 창측</figcaption></figure>
    <figure><img src="img/room-1p-c.jpg" alt="1인실 창가 책상과 의자" loading="lazy"><figcaption>1인실 창측, 다른 호실</figcaption></figure>
    <figure><img src="img/room-2p.jpg" alt="2인실 — 책상 2개와 창" loading="lazy"><figcaption>2인실 창측</figcaption></figure>
  </div>
  <h2>호실과 요금</h2>{PRIVATE_TABLE}
</div></section>
<section class="alt"><div class="wrap">
  <h2>상가 사무실과 무엇이 다른가</h2>
  <ul class="compare">
    <li>상가 임대는 보증금·관리비·인테리어·가구가 별도입니다. 여기는 책상·의자·인터넷·냉난방이 준비된 상태로 입주 당일부터 일합니다.</li>
    <li>상가 임대는 보통 1~2년 계약입니다. 여기는 월 단위로 시작하고, 사업이 커지면 2인실로 옮깁니다.</li>
    <li>언제든 출입합니다. 24시간 출입 시스템으로 주말·야간 작업이 가능합니다.</li>
  </ul>
</div></section>
<section><div class="wrap">
  <h2>이런 분께 맞습니다</h2>
  <div class="tags"><span>통화가 많은 영업·상담 직종</span><span>유튜브·온라인 강의 촬영</span><span>직원 1명 채용 직후</span><span>강일리버파크에서 걸어오는 분</span><span>미사·고덕에서 차로 오는 분</span></div>
</div></section>
{cta("빈 방은 사진보다 직접 보는 게 빠릅니다","톡톡으로 방문 시간을 남겨주시면 현재 빈 방을 보여드립니다.")}
""")

# ---------- 라운지 ----------
pages["lounge.html"] = dict(
 title="강일동 라운지 고정석 월 10만원부터 | 카페 대신 내 책상, 오피스워크넷 고덕강일점",
 desc="강일동 공유오피스 고정석. 재택근무·프리랜서를 위한 내 책상 하나, 월 10만원부터. 강일리버파크·미사에서 가까운 공간.",
 active="lounge.html",
 body=f"""
<div class="wrap"><p class="breadcrumb">홈 › 라운지 고정석</p></div>
<div class="page-head wrap"><h1>강일동 라운지 고정석 — 카페 대신 내 책상, 월 10만원부터</h1>
<p class="lead">강일리버파크나 미사에서 재택근무를 하다 보면 집과 일이 섞입니다. 카페는 하루 커피값만 월 10만원이 넘고, 자리도 매번 달라집니다. 라운지 고정석은 내 이름이 붙은 책상 하나를 월 단위로 쓰는 방식입니다. 모니터와 짐을 두고 다닙니다.</p></div>
<section><div class="wrap">
  <div class="gallery two">
    <figure><img src="img/lounge.jpg" alt="라운지 고정석 — 부스형 좌석과 창가" loading="lazy"><figcaption>라운지 좌석과 창가</figcaption></figure>
    <figure><img src="img/entrance.jpg" alt="입구에서 본 라운지" loading="lazy"><figcaption>입구에서 본 라운지</figcaption></figure>
  </div>
  <h2>좌석과 요금</h2>{LOUNGE_TABLE}
</div></section>
<section class="alt"><div class="wrap">
  <h2>이런 분께 맞습니다</h2>
  <div class="tags"><span>재택근무자</span><span>프리랜서 디자이너·개발자·마케터</span><span>사무실 계약 전에 먼저 써보고 싶은 예비창업자</span></div>
</div></section>
{cta("빈자리 확인은 톡톡으로","원하시는 좌석 종류만 남겨주시면 현재 빈자리와 이용 방법을 안내해 드립니다.")}
""")

# ---------- 요금 ----------
pages["pricing.html"] = dict(
 title="오피스워크넷 고덕강일점 요금표 | 비상주·라운지·상주 사무실 가격",
 desc="강일동 공유오피스 요금표. 비상주 월 2만원, 고정석 월 10만원, 1인실 27만원, 2인실 40만원부터. 부가세 별도.",
 active="pricing.html",
 body=f"""
<div class="wrap"><p class="breadcrumb">홈 › 요금 안내</p></div>
<div class="page-head wrap"><h1>오피스워크넷 고덕강일점 요금표</h1>
<p class="lead">세 상품 요금을 한 페이지에 모았습니다. 모든 금액은 부가세 별도이고, 관리비·인터넷·냉난방은 월 요금에 포함됩니다.</p></div>
<section><div class="wrap">
  <h2>비상주 사무실</h2>{VIRTUAL_TABLE}
  <h2 style="margin-top:40px">라운지 고정석</h2>{LOUNGE_TABLE}
  <h2 style="margin-top:40px">상주 사무실</h2>{PRIVATE_TABLE}
  <h3>할인 안내</h3>
  <ul class="compare"><li>상주·라운지는 6개월 결제 시 6만원 할인, 1년 결제 시 1개월을 추가로 이용합니다.</li><li>비상주는 계약 기간이 길수록 월 요금이 내려갑니다. 3개월에서 1년으로 바꾸면 개인 기준 월 2만원이 줄어듭니다.</li><li>6개월 계약을 중도 해지하면 할인받은 금액을 보증금에서 정산합니다. 계약 전에 미리 안내합니다.</li></ul>
</div></section>
<section class="alt"><div class="wrap"><h2>자주 묻는 질문</h2>{faq_html()}</div></section>
{cta("어떤 상품이 맞는지 모르겠으면","톡톡으로 '하는 일'만 보내주세요. 맞는 상품 하나만 권해드립니다.")}
""" + faq_jsonld())

# ---------- 오시는 길 ----------
pages["location.html"] = dict(
 title="오시는 길·시설 안내 | 오피스워크넷 고덕강일점 (강일역 인근)",
 desc="오피스워크넷 고덕강일점 위치와 시설. 서울 강동구 아리수로93길, 강일역 도보권. 상주 사무실 12실, 라운지 고정석 9석, 24시간 출입.",
 active="location.html",
 body=f"""
<div class="wrap"><p class="breadcrumb">홈 › 오시는 길</p></div>
<div class="page-head wrap"><h1>오시는 길 · 시설 안내</h1>
<p class="lead">{ADDR}</p>
<div class="btn-row"><a class="btn btn-primary" href="{MAP}" target="_blank" rel="noopener">네이버 지도에서 보기</a></div></div>
<section><div class="wrap">
  <h2>시설</h2>
  <table><thead><tr><th>시설</th><th>안내</th></tr></thead><tbody>
  <tr><td>상주 사무실 12실</td><td>1인실·2인실. 책상·의자 기본 제공</td></tr>
  <tr><td>라운지 고정석 9석</td><td>라운지석·창가석·프리미엄석</td></tr>
  <tr><td>미팅룸</td><td>유리벽 미팅룸 1실. 예약 방식은 톡톡으로 안내</td></tr>
  <tr><td>탕비실</td><td>커피머신·정수기·복합기(프린터)</td></tr>
  <tr><td>우편물 보관함</td><td>도착 시 알림</td></tr>
  <tr><td>출입</td><td>24시간 무인 출입</td></tr>
  <tr><td>주차</td><td>본 건물 주차 불가. 건물 주변 공영주차장 2곳 유료 이용 — 강일동 공영주차장 5분당 150원, 강일동 노상주차장 5분당 250원</td></tr>
  </tbody></table>
  <h2 style="margin-top:40px">주차 안내</h2>
  <p>본 건물에는 주차가 불가합니다. 차로 오시는 분은 건물 주변 공영주차장 2곳을 유료로 이용해 주세요. 두 곳 이름이 비슷하니 이용 전 주차장명을 꼭 확인하세요.</p>
  <table><thead><tr><th>주차장</th><th class="num">시간제 요금</th><th>비고</th></tr></thead><tbody>
  <tr><td>강일동 공영주차장</td><td class="num">150원 / 5분</td><td>경차·전기차·저공해차량 50% 할인 등 강동구 조례 기준</td></tr>
  <tr><td>강일동 노상주차장</td><td class="num">250원 / 5분</td><td>할인 기준 동일, 2건 이상 해당 시 높은 1건만 적용</td></tr>
  </tbody></table>
  <figure class="post-img" style="max-width:520px"><img src="img/parking.jpg" alt="오피스워크넷 고덕강일점 주차 안내 — 강일동 공영주차장 150원/5분, 노상주차장 250원/5분" loading="lazy"><figcaption>주차 안내 (2026년 7월 기준)</figcaption></figure>
  <h2 style="margin-top:40px">사진</h2>
  <div class="gallery">
    <figure><img src="img/entrance.jpg" alt="오피스워크넷 고덕강일점 입구" loading="lazy"><figcaption>입구</figcaption></figure>
    <figure><img src="img/lounge.jpg" alt="라운지" loading="lazy"><figcaption>라운지</figcaption></figure>
    <figure><img src="img/meeting-room.jpg" alt="미팅룸" loading="lazy"><figcaption>미팅룸</figcaption></figure>
    <figure><img src="img/pantry.jpg" alt="탕비실 — 커피머신과 복합기" loading="lazy"><figcaption>탕비실·복합기</figcaption></figure>
  </div>
</div></section>
{cta()}
""")

# ---------- 블로그 ----------
posts = [
 dict(slug="고덕그라시움-1인-공유오피스", old="godeok-graciums-one-person-shared-office", date="2026-10-06",
  title="고덕그라시움 1인 공유오피스, 단지 근처에서 찾을 때 확인할 5가지",
  desc="고덕그라시움 근처에서 1인 공유오피스를 고를 때 확인할 다섯 가지와 강일동 공유오피스까지의 동선을 정리했습니다.",
  kw="고덕그라시움 1인 공유오피스",
  body="""
<p>고덕그라시움은 단지가 크고 상가도 넓지만, 정작 "혼자 일할 사무실"은 단지 안에서 구하기가 쉽지 않습니다. 상가 사무실은 1인 사업자에게 크고, 카페는 통화가 불편합니다. 그래서 고덕그라시움 1인 공유오피스를 검색하는 분이 늘고 있습니다. 이 글은 재택근무자, 프리랜서, 1인 법인 대표가 고덕그라시움 근처에서 공유오피스를 고를 때 확인할 다섯 가지를 정리한 것입니다.</p>
<h2>1. 집에서 얼마나 걸리는가</h2>
<p>공유오피스는 매일 가는 곳입니다. 왕복 1시간이 넘으면 몇 달 안에 다시 집에서 일하게 됩니다. 고덕그라시움 기준으로는 상일동역·강일역 생활권, 즉 고덕동과 강일동 안에서 찾는 것이 현실적입니다. 점심에 집에 다녀올 수 있는 거리라면 재택과 출근의 장점을 둘 다 가져갈 수 있습니다.</p>
<h2>2. 1인실인가, 고정석인가</h2>
<figure class="post-img"><img src="../img/room-1p-window.jpg" alt="고덕그라시움 인근 1인 공유오피스 1인실 창측" loading="lazy"><figcaption>오피스워크넷 고덕강일점 1인실 창측. 문이 닫히는 독립 공간입니다.</figcaption></figure>
<p>"1인 공유오피스"라고 해도 두 종류가 있습니다. 문이 닫히는 독립 1인실과, 라운지 안에 내 책상 하나를 두는 고정석입니다. 상담 전화가 많거나 화상회의가 잦으면 1인실, 노트북 작업 위주면 고정석이 맞습니다. 고정석은 비용이 1인실의 절반 이하라서, 통화가 적은 분이 굳이 1인실을 쓸 이유는 없습니다.</p>
<h2>3. 월 요금에 무엇이 포함되는가</h2>
<p>관리비, 인터넷, 냉난방, 책상·의자가 포함인지 확인하세요. 상가 사무실은 이 항목이 전부 따로 붙습니다. 오피스워크넷 고덕강일점 기준으로 1인실은 내측 월 27만원, 창측 월 35만원, 라운지 고정석은 월 10만원부터이고 위 항목이 모두 포함입니다. 사업자등록 주소만 필요하면 비상주 월 2만원부터입니다. (모든 금액 부가세 별도)</p>
<h2>4. 계약 기간과 해지 조건</h2>
<p>1인 사업은 반년 뒤를 알기 어렵습니다. 1년 이상 묶이는 계약보다 월 단위로 시작해서 사업이 자리 잡으면 6개월·1년 결제로 바꾸는 쪽이 안전합니다. 장기 결제 할인이 있는지, 중간에 라운지석에서 1인실로 옮길 수 있는지도 미리 물어보세요.</p>
<h2>5. 운영자가 같은 건물에 있는가</h2>
<p>우편물 수령, 출입 문제, 계약 변경은 운영자가 상주해야 그날 해결됩니다. 무인으로만 운영되는 곳은 작은 일이 며칠씩 걸립니다. 계약 전에 "관리자가 어디 계시냐"를 꼭 물어보세요.</p>
<h2>고덕그라시움에서 오피스워크넷 고덕강일점까지</h2>
<figure class="post-img"><img src="../img/lounge-desks.jpg" alt="강일동 공유오피스 라운지 고정석 창가 자리" loading="lazy"><figcaption>라운지 고정석 창가 자리. 모니터와 짐을 두고 다닙니다.</figcaption></figure>
<p>오피스워크넷 고덕강일점은 고덕그라시움과 같은 5호선 생활권인 강일동 강일프라자 5층에 있습니다. 고덕동에서 차로 가까운 거리이고, 대중교통은 상일동역 다음 정거장인 강일역을 이용합니다. 본 건물에는 주차가 되지 않아 차로 오실 때는 인근 강일동 공영주차장을 이용하셔야 하는 점은 미리 알려드립니다.</p>
<blockquote>정리하면, 고덕그라시움에서 1인 공유오피스를 찾는다면 "거리 → 1인실인지 고정석인지 → 포함 항목 → 계약 조건 → 운영자 상주" 순서로 확인하면 실패가 적습니다.</blockquote>
<h2>빈자리 확인</h2>
<p>1인실과 고정석은 사진보다 직접 보는 게 빠릅니다. 톡톡으로 "고덕그라시움에서 가요, 1인실(또는 고정석) 보고 싶어요"라고 남겨주시면 현재 빈자리와 방문 가능한 시간을 안내해 드립니다.</p>
"""),
 dict(slug="강일동-공유오피스", old="gangil-dong-shared-office", date="2026-09-29",
  title="강일동 공유오피스, 집에서 걸어가는 사무실은 어디 있을까",
  desc="강일동에서 사무실을 찾을 때 상가 임대·카페·공유오피스 세 가지를 월 비용과 계약 조건으로 비교했습니다.",
  kw="강일동 공유오피스",
  body="""
<p>강일동은 아파트 단지가 많고 상가 사무실은 적습니다. 그래서 강일리버파크나 고덕 쪽에 사는 1인 사업자가 "집 근처 사무실"을 검색하면 결과가 몇 개 안 나옵니다. 이 글은 강일동에서 사무 공간을 구하는 세 가지 방법을 월 비용과 계약 조건으로 비교한 것입니다.</p>
<h2>1. 상가 사무실 임대</h2>
<p>강일동 상가 소형 사무실은 보증금과 월세 외에 관리비, 인터넷, 냉난방비가 따로 붙습니다. 책상과 의자도 직접 사야 합니다. 계약은 보통 1년 이상이고, 사업이 안 풀려도 기간을 채워야 합니다. 혼자 일하는 사업자에게는 공간이 남고 비용은 넘칩니다.</p>
<h2>2. 카페</h2>
<p>처음 몇 달은 카페로 버틸 수 있습니다. 문제는 전화입니다. 상담 전화, 거래처 통화를 카페에서 받다 보면 자리를 옮기거나 밖으로 나가야 합니다. 하루 커피 두 잔이면 월 10만원이 넘고, 자리는 매번 다릅니다.</p>
<h2>3. 공유오피스</h2>
<figure class="post-img"><img src="../img/room-1p-a.jpg" alt="강일동 공유오피스 1인실 창측" loading="lazy"><figcaption>오피스워크넷 고덕강일점 1인실 창측</figcaption></figure>
<p>공유오피스는 세 가지로 나뉩니다. 주소만 쓰는 비상주(월 2만원부터), 내 책상 하나를 쓰는 라운지 고정석(월 10만원부터), 문 닫히는 독립 사무실(1인실 월 27만원부터). 관리비·인터넷·냉난방이 월 요금에 포함되고, 월 단위로 시작할 수 있습니다. (모든 금액 부가세 별도)</p>
<blockquote>정리하면, 통화가 많고 집중이 필요하면 1인실, 노트북 작업 위주면 고정석, 사업자등록 주소만 필요하면 비상주입니다.</blockquote>
<h2>운영자 입장에서 본 한 가지</h2>
<p>공유오피스를 고를 때 요금표보다 먼저 볼 것은 "누가 관리하는가"입니다. 관리자가 상주하지 않는 곳은 우편물, 출입 문제, 계약 변경이 며칠씩 걸립니다. 운영자가 같은 건물에 있는지 계약 전에 물어보세요.</p>
"""),
 dict(slug="강일리버파크-공유오피스-고정석", old="gangil-riverpark-freelancer-desk", date="2026-09-29",
  title="강일리버파크 사는 프리랜서가 카페 대신 고정석을 선택한 이유",
  desc="강일리버파크에서 재택근무를 하던 프리랜서가 라운지 고정석으로 옮기면서 달라진 세 가지.",
  kw="강일리버파크 공유오피스",
  body="""
<p>강일리버파크에서 재택근무를 3년쯤 하면 공통으로 겪는 일이 있습니다. 아이가 하교하면 일이 끊기고, 저녁에 다시 노트북을 켜면 밤 12시가 됩니다. 집과 일이 섞이는 것입니다.</p>
<h2>카페로 나갔던 시기</h2>
<p>처음에는 단지 앞 카페로 나갔습니다. 문제는 세 가지였습니다. 자리가 매번 달라 모니터를 못 쓰고, 통화가 오면 밖으로 나가야 하고, 하루 두 잔이면 월 커피값이 10만원을 넘었습니다.</p>
<h2>고정석으로 옮긴 뒤 달라진 것</h2>
<figure class="post-img"><img src="../img/lounge.jpg" alt="강일동 라운지 고정석" loading="lazy"><figcaption>라운지 고정석. 모니터와 짐을 두고 다닙니다.</figcaption></figure>
<p>첫째, 모니터와 키보드를 두고 다닙니다. 출근하면 바로 일이 시작됩니다. 둘째, 퇴근이 생겼습니다. 사무실을 나오면 일이 끝납니다. 셋째, 비용이 카페와 비슷하거나 낮습니다. 라운지석 월 10만원(부가세 별도)은 카페 커피값과 크게 다르지 않습니다.</p>
<blockquote>고정석은 사무실을 빌리는 게 아니라 "출퇴근"을 사는 것에 가깝습니다.</blockquote>
<h2>강일리버파크에서의 거리</h2>
<p>오피스워크넷 고덕강일점은 강일리버파크에서 걸어갈 수 있는 거리, 강일역 인근입니다. 점심에 집에 다녀올 수 있는 거리라는 점이 재택근무자에게는 중요합니다. 빈자리와 이용 방법은 톡톡으로 물어보세요.</p>
"""),
 dict(slug="강일동-1인사무실-월비용", old="gangil-dong-one-person-office-cost", date="2026-09-29",
  title="강일동 1인사무실 월 비용, 상가 임대와 공유오피스 비교",
  desc="강일동 1인 사무실을 구할 때 상가 임대와 공유오피스 1인실의 월 총비용을 항목별로 비교했습니다.",
  kw="강일동 1인사무실",
  body="""
<p>"강일동 1인사무실"을 검색하면 월세만 보고 판단하기 쉽습니다. 실제 월 비용은 월세에 관리비, 인터넷, 냉난방, 가구 감가, 보증금 이자까지 더해야 나옵니다. 항목별로 나눠 보겠습니다.</p>
<h2>상가 사무실 1인 기준 월 비용 항목</h2>
<p>월세 외에 관리비(건물마다 다름), 인터넷 회선, 여름·겨울 냉난방 전기료, 책상·의자 구입비를 월로 환산한 금액, 그리고 보증금이 묶이는 기회비용이 있습니다. 여기에 1년 이상 계약이 붙습니다.</p>
<h2>공유오피스 1인실 월 비용 항목</h2>
<figure class="post-img"><img src="../img/room-1p-c.jpg" alt="강일동 1인사무실 창가" loading="lazy"><figcaption>1인실 창측. 책상·의자가 준비된 상태로 입주합니다.</figcaption></figure>
<p>월 요금 하나입니다. 오피스워크넷 고덕강일점 기준 1인실 내측 27만원, 창측 35만원(부가세 별도)이고 관리비·인터넷·냉난방·가구가 포함됩니다. 6개월 결제 시 6만원 할인, 1년 결제 시 1개월 추가입니다.</p>
<h2>비교표</h2>
<table><thead><tr><th>항목</th><th>상가 사무실</th><th>공유오피스 1인실</th></tr></thead><tbody>
<tr><td>보증금</td><td>있음</td><td>소액 또는 없음 (계약 시 안내)</td></tr>
<tr><td>관리비·인터넷·냉난방</td><td>별도</td><td>포함</td></tr>
<tr><td>가구</td><td>직접 구입</td><td>포함</td></tr>
<tr><td>계약 기간</td><td>보통 1~2년</td><td>월 단위 시작</td></tr>
<tr><td>출입</td><td>건물 규정</td><td>24시간</td></tr>
</tbody></table>
<blockquote>월세 숫자만 보면 상가가 싸 보일 때가 있지만, 항목을 다 더하면 1인 사업자는 공유오피스 1인실이 낮게 나오는 경우가 많습니다. 정확한 비교는 본인이 보는 상가 매물의 관리비를 넣어 계산해 보세요.</blockquote>
<h2>강일동에서 직접 보려면</h2>
<p>빈 방은 사진보다 직접 보는 게 빠릅니다. 톡톡으로 방문 시간을 남겨주시면 현재 빈 1인실을 보여드립니다.</p>
"""),
]

def post_page(p):
    linkbox = f'<div class="link-box"><strong>오피스워크넷 고덕강일점</strong>서울 강동구 강일동, 강일역 인근. 비상주 월 2만원~, 라운지 고정석 월 10만원~, 1인실 월 27만원~ (부가세 별도).<br><a class="btn btn-primary" style="margin-top:12px" href="{TALK}" target="_blank" rel="noopener">네이버 톡톡으로 묻기</a> <a class="btn btn-outline" style="margin-top:12px" href="../pricing.html">요금표 보기</a></div>'
    body = f"""
<div class="wrap"><p class="breadcrumb"><a href="../index.html">홈</a> › <a href="index.html">오피스 소식</a></p>
<article class="post"><h1>{p['title']}</h1><div class="meta"><time datetime="{p['date']}">{p['date']}</time> · {BRAND}</div>
{p['body']}{linkbox}</article></div>
"""
    import json
    jsonld = '<script type="application/ld+json">' + json.dumps({"@context":"https://schema.org","@type":"BlogPosting","headline":p["title"],"description":p["desc"],"datePublished":p["date"],"author":{"@type":"Organization","name":BRAND}}, ensure_ascii=False) + '</script>'
    return dict(title=f"{p['title']} | {BRAND}", desc=p['desc'], active="blog/index.html", body=body, jsonld=jsonld)

for p in posts:
    pages[f"blog/{p['slug']}.html"] = post_page(p)
    if p.get("old"):
        os.makedirs(f"{OUT}/blog", exist_ok=True)
        with open(f"{OUT}/blog/{p['old']}.html","w",encoding="utf-8") as rf:
            rf.write(f'<!doctype html><meta charset="utf-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url={quote(p["slug"])}.html"><link rel="canonical" href="{SITE_URL}/blog/{quote(p["slug"])}.html"><a href="{quote(p["slug"])}.html">이동</a>')

pages["blog/index.html"] = dict(
 title="오피스 소식 | 오피스워크넷 고덕강일점",
 desc="강일동·고덕·미사 사무실, 비상주 사무실, 사업자등록에 대해 운영자가 직접 씁니다.",
 active="blog/index.html",
 body=f"""
<div class="wrap"><p class="breadcrumb"><a href="../index.html">홈</a> › 오피스 소식</p></div>
<div class="page-head wrap"><h1>오피스 소식</h1><p class="lead">강일동·고덕·미사에서 사무실을 찾는 분, 사업자등록 주소가 필요한 분이 궁금해하는 것을 운영자가 직접 씁니다.</p></div>
<section><div class="wrap"><div class="post-list">
{"".join(f'<article><time datetime="{p["date"]}">{p["date"]}</time><h3><a href="{quote(p["slug"])}.html">{p["title"]}</a></h3><p>{p["desc"]}</p></article>' for p in posts)}
</div></div></section>
{cta()}
""")

# ---------- 출력 ----------
os.makedirs(f"{OUT}/blog", exist_ok=True)
for path, pg in pages.items():
    canonical = f"{SITE_URL}/{'' if path=='index.html' else quote(path)}"
    with open(f"{OUT}/{path}", "w", encoding="utf-8") as f:
        f.write(layout(pg["title"], pg["desc"], pg["body"], path, canonical, pg.get("active",""), pg.get("jsonld","")))
import shutil; shutil.copy("style.css", f"{OUT}/style.css")
EXTRA_CSS = """
/* 푸터 위 여백: 본문 마지막 요소가 푸터에 붙지 않도록 */
footer.site{margin-top:64px}
section.cta+footer.site{margin-top:0}
article.post{padding-bottom:8px}
.post-list{margin-bottom:16px}
@media (max-width:820px){footer.site{margin-top:48px}}
"""
with open(f"{OUT}/style.css","a",encoding="utf-8") as f: f.write(EXTRA_CSS)
if os.path.isdir("img"): shutil.copytree("img", f"{OUT}/img", dirs_exist_ok=True)

with open(f"{OUT}/sitemap.xml","w",encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for path in pages:
        loc = f"{SITE_URL}/{'' if path=='index.html' else quote(path)}"
        f.write(f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod></url>\n")
    f.write("</urlset>\n")
with open(f"{OUT}/robots.txt","w",encoding="utf-8") as f:
    f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
with open(f"{OUT}/rss.xml","w",encoding="utf-8") as f:
    f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>{BRAND} 오피스 소식</title><link>{SITE_URL}/blog/index.html</link><description>강일동·고덕·미사 사무실과 사업자등록 이야기</description>\n')
    for p in posts:
        f.write(f"<item><title>{html.escape(p['title'])}</title><link>{SITE_URL}/blog/{quote(p['slug'])}.html</link><description>{html.escape(p['desc'])}</description><pubDate>{p['date']}</pubDate></item>\n")
    f.write("</channel></rss>\n")
open(f"{OUT}/.nojekyll","w").close()
print("generated", len(pages), "pages →", OUT)
