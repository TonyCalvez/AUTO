
s = tf('s');

P = 1/(s+1)^3;

Kp = 1;
Ki = 0;
Kd = 0;

C = (Kp*s+Ki+Kd*s^2)/s;

L = P*C;
figure; step(L/(1+L));

figure; hold on; margin(L); margin(L/(1+L)); legend('L', 'L/(1+L)');
figure; hold on; nyquist(L); nyquist(L/(1+L)); legend('L', 'L/(1+L)');
figure; hold on; nichols(L); nichols(L/(1+L)); legend('L', 'L/(1+L)');