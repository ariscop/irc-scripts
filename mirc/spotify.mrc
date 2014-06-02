
alias spotifynp {
    var %ignorethis = $regex(spotify,$dll(spotify,mircFindWindow,Spotify - ),/Spotify - (.+)/)
    return $regml(spotify, 1)
}

alias setnp {
    if (%lastnp != $spotifynp) {
        set %lastnp $v2
        /np
    }
}

alias startnp {
    timerspotify 0 1 setnp
}

alias stopnp {
    timerspotify off
}

alias np {
    me is now playing $spotifynp
}
