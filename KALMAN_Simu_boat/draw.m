function draw(x,u)
% Global variables to share with other files.
global L, global l, global alpha, global beta;
v = alpha*u(1);
delta = beta*u(2);
M=[-L/2 -L/2    -0.2     0.2 L/2-0.1     L/2      L/2 L/2-0.1     0.2      -0.2 -L/2;
   -l/2  l/2 l/2+0.1 l/2+0.1     l/2 l/2-0.1 -l/2+0.1    -l/2 -l/2-0.1 -l/2-0.1 -l/2;
    ones(1,11)]; % Motif du tube principal.
G=[-0.2 0;
      0 0;
      1 1]; % Motif du gouvernail.
R=[cos(x(3)),-sin(x(3)),x(1);sin(x(3)),cos(x(3)),x(2);0 0 1];
M=R*M;
G=R*[cos(-delta),-sin(-delta) -L/2;sin(-delta),cos(-delta) 0;0 0 1]*G;
plot(M(1,:),M(2,:),'b');
plot(G(1,:),G(2,:),'k');
end
