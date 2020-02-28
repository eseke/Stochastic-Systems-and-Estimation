close all
g = 100000; %broj eksperimenata
g1 = 100; %broj stubaca u histogramu

a = rand(1,g);
for i =1:g
    if a(1,i)<=1/2
        a(1,i) = -sqrt(1-2*a(1,i));
    else
        a(1,i) = sqrt(2*a(1,i)-1);
    end
end
histogram(a,g1,'Normalization','Probability');

n = [-1 0 0 1];
k = [1/(g1/2) 0 0 1/(g1/2)];

hold all
plot(n,k,'--','LineWidth',3);
title('Funkcija gustine verovatnoce');
xlabel('Ishod X=k');
ylabel('Vrednost funkcije gustine veroratnoce');
legend('eksperimentalna vrednost','egzaktna vrednost');

m = sum(a)/g;
e = (sum((a-m).^2))/(99999);