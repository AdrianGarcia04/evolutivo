tx = ty = linspace (-600, 600, 100)';
[xx, yy] = meshgrid (tx, ty);
a = 20;
b = 0.2;
c = 2 * pi;
d = 2;

sum1 = 0;
for
  sum1 = sum1 + (xx .^ 2 + yy .^2) ./ 4000;
endfor

prod1 = 1;
ind = 1;
for
  prod1 = prod * cos((xx) ./ sqrt(ind));
  ind = ind + 1;
endfor

tz = sum1 - prod1 + 1;
mesh (tx, ty, tz);
xlabel ("tx");
ylabel ("ty");
zlabel ("tz");
title ("Ackley function");