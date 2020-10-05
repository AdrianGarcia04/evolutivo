tx = ty = linspace (-10, 10, 200)';
[xx, yy] = meshgrid (tx, ty);
a = 20;
b = 0.2;
c = 2 * pi;
d = 2;

sum1 = 0;
for
  sum1 = (xx .^ 2) + (yy .^2);
endfor

sum2 = 0;
for
  sum2 = cos(2 * pi * xx) + cos(2 * pi * yy);
endfor

tz = - a * exp(-b * sum1 ./ d) - exp(sum2 ./ d) + a + exp(1);
mesh (tx, ty, tz);
xlabel ("tx");
ylabel ("ty");
zlabel ("tz");
title ("Ackley function");