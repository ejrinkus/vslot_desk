from solid import *
from solid.utils import *  # Not required, but the utils module is useful
from cbeam import *
from vslot2020 import *
from vslot4040 import *

def in_to_mm(inches):
    return inches*25.4;

# Constants
DESK_WIDTH_IN=72;
DESK_DEPTH_IN=39;
DESK_THICKNESS_IN=1.5;
DESK_HEIGHT_IN=30;

DESK_WIDTH=in_to_mm(DESK_WIDTH_IN);
DESK_DEPTH=in_to_mm(DESK_DEPTH_IN);
DESK_THICKNESS=in_to_mm(DESK_THICKNESS_IN);
DESK_HEIGHT=in_to_mm(DESK_HEIGHT_IN);

RAIL_WIDTH=40;
RAIL_HEIGHT=80;
RAIL_THICKNESS=20;
RAIL_GAP_WIDTH=RAIL_WIDTH - RAIL_THICKNESS;
RAIL_GAP_HEIGHT=RAIL_HEIGHT - (2*RAIL_THICKNESS);
LEG_THICKNESS=40;

WALNUT_COLOR=[93/255, 67/255, 44/255];

# Desktop
def make_desktop():
    # Make the actual desktop object, raise it to the proper height, and shift it to the right to
    # make room for the left rail.
    desktop = up(DESK_HEIGHT)(
        right(RAIL_THICKNESS)(
            color(WALNUT_COLOR)(
                cube([DESK_WIDTH, DESK_DEPTH, DESK_THICKNESS])
            )
        )
    );

    # Cut a notch in the two back corners of the desk to make room for the two back legs.
    desktop -= forward(DESK_DEPTH - 20)(
        up(DESK_HEIGHT)(
            right(20)(
                cube([20, 20, DESK_THICKNESS])
            )
        )
    );
    desktop -= forward(DESK_DEPTH - RAIL_GAP_WIDTH)(
        up(DESK_HEIGHT)(
            right(RAIL_THICKNESS)(
                cube([RAIL_GAP_WIDTH, RAIL_GAP_WIDTH, DESK_THICKNESS])
            )
        )
    );

    return desktop

# C-Beam rails surrounding desktop
def make_left_rail():
    left_rail = up(80 + DESK_HEIGHT - 20)(
        rotate([-90, 0, 0])(
            make_cbeam(DESK_DEPTH - 20)
        )
    );
    return left_rail;

def make_right_rail():
    right_rail = up(DESK_HEIGHT - 20)(
        right(DESK_WIDTH + 40)(
            rotate([-90, 180, 0])(
                make_cbeam(DESK_DEPTH - 20)
            )
        )
    );
    return right_rail;

def make_back_rail():
    back_rail = right(40)(
        forward(20 + DESK_DEPTH)(
            up(60 + DESK_HEIGHT)(
                rotate([-90, 0, -90])(
                    make_cbeam(DESK_WIDTH - 40)
                )
            )
        )
    );
    return back_rail;

# 4040 legs
def make_front_left_leg():
    leg = make_4040(DESK_HEIGHT - 20);
    return leg;

def make_front_right_leg():
    leg = right(DESK_WIDTH)(
        make_4040(DESK_HEIGHT - 20)
    );
    return leg;

def make_back_left_leg():
    leg = forward(DESK_DEPTH - 20)(
        make_4040(DESK_HEIGHT + 60 + in_to_mm(30))
    );
    return leg;

def make_back_right_leg():
    leg = forward(DESK_DEPTH - 20)(
        right(DESK_WIDTH)(
            make_4040(DESK_HEIGHT + 60 + in_to_mm(30))
        )
    );
    return leg;

def make_desk():
    desk = make_desktop();
    desk += make_left_rail();
    desk += make_right_rail();
    desk += make_back_rail();
    desk += make_front_left_leg();
    desk += make_front_right_leg();
    desk += make_back_left_leg();
    desk += make_back_right_leg();
    return desk;

scad_render_to_file(make_desktop(), '../desktop.scad');
scad_render_to_file(make_desk(), '../desk.scad');