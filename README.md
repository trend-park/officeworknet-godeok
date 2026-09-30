# 오피스워크넷 고덕강일점 사이트

GitHub Pages용 정적 사이트. `build.py`가 `docs/` 폴더에 HTML을 생성합니다.

## 배포 (처음 한 번)
1. GitHub에서 새 저장소 `officeworknet-godeok` 생성 (Public)
2. 이 폴더 전체 업로드 (docs 폴더 포함)
3. 저장소 Settings → Pages → Source: `Deploy from a branch`, Branch: `main` / 폴더: `/docs` → Save
4. 1~2분 후 `https://<계정명>.github.io/officeworknet-godeok/` 에서 확인

## 배포 후 반드시 할 것
- `build.py` 상단 `SITE_URL`을 실제 주소로 바꾸고 다시 `python3 build.py` → sitemap·canonical이 맞춰집니다
- `TALK`에 네이버 톡톡 링크, `ADDR`에 번지·건물명, `NAVER_VERIFY`에 서치어드바이저 메타 값 입력
- 네이버 서치어드바이저(searchadvisor.naver.com)에 사이트 등록 → 소유확인 → `sitemap.xml`, `rss.xml` 제출
- 네이버 스마트플레이스 '홈페이지' 항목에 이 주소 입력

## 글 추가
`build.py`의 `posts` 리스트에 항목을 추가하고 `python3 build.py` 실행 → 블로그 목록·sitemap·rss가 자동 갱신됩니다.
