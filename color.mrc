
/*
 * boton/botoff: Enable/Disable talking through chanserv
 * coloron/coloroff: Enable/Disable colors
 * colorset: Set color (ie: /colorset 00,02)
 */ 

alias boton { set -n %bot on }
alias botoff { unset %bot }
alias coloron { set -n %coloren on }
alias coloroff { unset %coloren }
alias colorset { set %color $1 }
on *:INPUT: #Bronystate, #bronystate_ru, #bronystateregulars, #Twilight_Sparkle, #Rainbow_Dash, #Pinkie_Pie, #Applejack, #Rarity, #Fluttershy, #Vinyl_Scratch, #Derpy_Hooves: {
    if ($left($1,1) != /) {
        set %msgrbw $1-
        if (%coloren) {
            set %msgrbw $chr(3) $+ %color $+ $1-
        }
        if (%bot) {
            msg BotServ say $chan %msgrbw
        }
        else {
            msg $chan %msgrbw
        }
        haltdef
    }
}
