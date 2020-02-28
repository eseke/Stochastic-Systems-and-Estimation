X = zeros(2,10000);
X(1,:) = randn(1,10000);
X(2,:) = randn(1,10000);

Ay = [2.2/sqrt(2) sqrt(3-2.42);sqrt(2) 0];
Az = [0 sqrt(3);sqrt(5/3) -1/sqrt(3)];
Y = Ay*X;
Z = Az*X;

figure(1)
scatter(X(1,:),X(2,:),'filled');
title('Odbirci slucajnog vektora X');
xlabel('X1');
ylabel('X2');

figure(2)
scatter(Y(1,:),Y(2,:),'filled');
title('Odbirci slucajnog vektora Y');
xlabel('Y1');
ylabel('Y2');

figure(3)
scatter(Z(1,:),Z(2,:),'filled');
title('Odbirci slucajnog vektora Z');
xlabel('Z1');
ylabel('Z2');