% This function should be called when a key is pressed.
function keycontrol()
% Global variables to share with other files.
global u;
global bExit;
global scale, global offsetx, global offsety;
key = get(gcbf,'CurrentCharacter');
% Actions to do depending on the key pressed.
switch (key)
    case 27,
        bExit = 1;
    case 'z',
        u(1) = u(1)+0.1;
        if (u(1) > 1) u(1) = 1; end
    case 's',
        u(1) = u(1)-0.1;
        if (u(1) < -1) u(1) = -1; end
    case 'q',
        u(2) = u(2)+0.1;
        if (u(2) > 1) u(2) = 1; end
    case 'd',
        u(2) = u(2)-0.1;
        if (u(2) < -1) u(2) = -1; end
    case ' ',
        u = [0;0];
    case '+',
        scale = scale*0.9;
    case '-',
        scale = scale/0.9;
    case 'i',
        offsety = offsety+1;
    case 'k',
        offsety = offsety-1;
    case 'l',
        offsetx = offsetx+1;
    case 'j',
        offsetx = offsetx-1;
end
end
