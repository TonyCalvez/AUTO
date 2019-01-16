function xdot = f(x,u)
%  variables to share with other files.
xdot = [x(4)*cos(x(5))*cos(x(3));
        x(4)*cos(x(5))*sin(x(3));
        x(4)*sin(x(5))/3;
        u(1);
        u(2);
        ];
end


