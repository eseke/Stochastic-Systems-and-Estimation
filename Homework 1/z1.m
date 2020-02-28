a = rand(1,1000); % a - niz od 1000 bacanja 4 - strane kocke

for i = 1:1000
    if a(1,i)<=1/6
        a(1,i) = 1;
    elseif a(1,i)<=1/2
        a(1,i) = 2;
    elseif a(1,i)<=2/3
        a(1,i) = 3;
    else
        a(1,i) = 4;
    end
end

figure(1)
histogram(a);
title('Histogram generisanih ishoda');
xlabel('Ishod X=k');
ylabel('Broj odgovarajucih povoljnih ishoda');

b1 = [0 1/6 1/3 1/6 1/3]; % b1 - egzaktne vrednosti mase verovatnoce
b = zeros(1,5); % b - eksperimentalne vrednosti mase verovatnoce

for i = 1:4
   b(1,i+1) = sum(a==i)/1000;
end

figure(2)
plot(0:4,b1,'--',0:4,b);
title('Funkcija mase verovatnoce');
xlabel('Ishod X=k');
ylabel('Vrednost funkcije mase verovarnoce');
legend('egzaktna vrednost','eksperimentalna vrednost');

c1 = [0 1/6 1/2 2/3 1]; % egzaktne vrednosti funkcije raspodele
c = zeros(1,5); % c - eksperimentalne vrednosti funkcije raspodele

for i = 1:4
    c(1,i+1) = c(1,i) + b(1,i+1);
end

figure(3)
plot(0:4,c1,'--',0:4,c);
title('Funkcija raspodele');
xlabel('Ishod X=k');
ylabel('Vrednost funkcije raspodele');
legend('egzaktna vrednost','eksperimentalna vrednost');

d = sum(a)/1000 % d - matematicko ocekivanje
e = (sum((a-d).^2))/(999) % e - varijansa