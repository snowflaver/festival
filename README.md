# 트러블
### 2023 - 05 - 12
```
import styled from "styled-components";

const Backarea = styled.div`
display: flex;
flex-direction: column;
align-items: center;
justify-content: flex-start;
padding-top: 20px;
`

export { Backarea }
```
해당 스타일을
```
import React from "react";
//...

function Mainlogin() {
  return (
    <Backarea>
      <Login />
      <Stringsignupbutton />
    </Backarea>
  )
}

export default Mainlogin;
```
이렇게 구성햇는데

![image](https://github.com/snowflaver/trubleshot/assets/121342379/84349390-b9f6-415a-88f7-8b6371619fe6)

이렇게 `<Login />`과 `<Stringsignupbutton />`사이가 안좁혀진다....

### 2023 - 05 - 13
오늘 트러블은 에러메세지를 상태메세지로 사용자에게 보여지게 만드는것이다.
먼저 하고자햇던 답안지는

![image](https://github.com/snowflaver/trubleshot/assets/121342379/5891f24c-4323-4ffc-a564-bff7add62386)


이렇게 하는게 목표엿지만 에러메세지를 만들어봣지만 안나왓다....

# 트러블 슈팅
### 2023 - 05 - 12
오늘 드디어 해결을 했다.

![image](https://github.com/snowflaver/trubleshot/assets/121342379/21688e1a-7ae5-4cfb-ab31-c014e3f4c5f5)

처음에는 구글검색해서 찾아보려햇지만 현재 상태를 전달해줄 방법이 없어서
가까운 동료에게 가서 도움을 요청햇다.
그 분이 알려주신 방법음 개발자도구에서 컴포넌트?블록?을 확인해보라고 해서 확인햇더니.....

![image](https://github.com/snowflaver/trubleshot/assets/121342379/434f985d-f84f-4b6f-a502-93b85043fd5a)

(이건 미쳐사진찍어두지못해서 예시사진이다.)

이렇게 나오는것이 아닌가...여기서 문제를 발견햇다 하나의 블록안에 형성된거이 아니라 블록과 블록을 붙이고 있엇던 것이다.
```
    <Backarea>
      <Login />
      <Stringsignupbutton />
    </Backarea>
```
이 코드처럼 블록끼리 붙이고 있어서 뭘하려해고 블록과 블록으로 가지고 하는것이엇기에
<Stringsignupbutton />이것을 <Login />안에 집어넣엇더니 해결이 되엇다...!
