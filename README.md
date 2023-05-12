# 트러블
### 2023- 05- 12
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
