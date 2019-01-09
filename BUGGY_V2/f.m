function [xdot] = f(x,u)
alpha = 1; beta = 1; L=1;
v=alpha*u(1); delta=beta*u(2);
xdot = [v*cos(delta)*cos(x(3));
        v*cos(delta)*sin(x(3));
        v*sin(delta)/L];
end