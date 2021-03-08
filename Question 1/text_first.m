clc
clear all
close all

m=9;
n=9;

A=zeros(m,n);
for k=1:m
    A(k,:)=k;
end
B=zeros(m,1);
temp=(m-1)*m/2;
for k=1:m
    B(k)=temp+k*(n-1);
end
B(1)
B(end)

N=input('请输入所求值：');

% 0 = Right && 1 = Down

C=zeros(m,m+n-2);
Eye=ones(1,n-1);

for k=1:m
    C(k,k:k+n-2)=Eye;
end

if B(B==N)
    D=find(B==N);
    result=C(D,:);
else
        D=max(find(B<N));
        Gap=N-B(D);
        F=C(D,:);
        exchange=max(find(F,1,'last'));
        F(exchange+1)=1;
        F(exchange-Gap+1)=0;
        result=F;
end
operations=[];
for k=1:m+n-2
    if result(k)==0
        operations=[operations,'D'];
    else 
        operations=[operations,'R'];
    end
end
disp(['The simplest operations is ' operations])