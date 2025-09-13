# 🤝 Contributing Guide

이 문서는 **Labor Law Assistant** 프로젝트에 기여하는 방법을 설명합니다.  
우리 팀이 협업할 때 지켜야 할 규칙들을 모아두었습니다.

---

## 🪜 브랜치 전략

- **main** : 배포용 / 안정 버전 (직접 push 금지)
- **dev** : 개발 통합 브랜치 (feature 작업물을 머지하는 곳)
- **feature/** : 기능 단위 브랜치  
  - 예시: `feature/chatbot-ui`, `feature/law-api`, `feature/firebase-setup`

---

## 🛠 작업 순서

1. dev 브랜치 최신화
```bash
git checkout dev    
git pull origin dev
```
2. 새 브랜치 생성
```bash
git checkout -b feature/기능명    
```
3. 코드 작성 -> 커밋 & 푸시
```bash
git add .    
git commit -m "feat: 챗봇 UI 기본 뼈대 추가"
git push origin feature/기능명
```
4. GitHub에서 Pull Request(PR) 생성
- feature/* → dev
- 리뷰 후 merge
5. dev → main 병합은 안정화 시점에만 진행


## 📝 커밋 메시지 규칙

| 타입 | 설명 |
|------|------|
| `feat:` | 새로운 기능 추가 |
| `fix:` | 버그 수정 |
| `docs:` | 문서 수정 |
| `style:` | 코드 스타일 변경 (동작 영향 없음) |
| `refactor:` | 리팩토링 |
| `test:` | 테스트 코드 |
| `chore:` | 설정/빌드 등 기타 작업 |

👉 예시:
- `feat: 노동법 조회 API 엔드포인트 추가`
- `fix: 챗봇에서 null 응답 처리 오류 수정`

## 📌 추가 규칙
- Python 코드는 PEP8 스타일을 권장합니다 (`black`, `autopep8` 사용 가능).
- 환경 변수는 `.env` 파일에 저장하고 `.gitignore`에 포함시켜야 합니다.
- Pull Request는 최소 1명 이상의 리뷰 후 merge합니다.
- 새로운 기능이나 버그 수정은 GitHub Issues를 생성하고, 해결되면 close합니다.