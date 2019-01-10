clear all;
close all;
figure;
hold on;

n = 100000;
x0 = randn(n,2)'; 
x0_bar = mean(x0');
G0 = cov(x0');

x_bar=[1;2]
Gx=[3    1;
    1   3]

x=x_bar*ones(1,n)+sqrtm(Gx)*x0;
plot(x(1,:), x(2,:), '.');

eta = [0.9 0.99 0.999];
draw_ellipse(x_bar, Gx, eta(1));
draw_ellipse(x_bar, Gx, eta(2));
draw_ellipse(x_bar, Gx, eta(3));

x_bar_verif = mean(x')
G_verif=cov(x')
