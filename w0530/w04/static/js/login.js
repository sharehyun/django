if ('{{msg}}'=='1'){
    alert('로그인 성공');
    location.href='/';
}
else if('{{msg}}'=='0'){
    alert('아이디 또는 패스워드가 일치하지 않습니다.');
}