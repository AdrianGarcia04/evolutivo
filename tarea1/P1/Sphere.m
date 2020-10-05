tx = ty = linspace (-5.12, 5.12)';
[xx, yy] = meshgrid (tx, ty);

sum = 0;
for
  sum = xx .^ 2 + yy .^2;
endfor

mesh (tx, ty, sum);
xlabel ("tx");
ylabel ("ty");
zlabel ("tz");
title ("Sphere function");