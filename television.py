class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__before = Television.MIN_VOLUME


    def power(self):
        """
        Changes the television status from on to off or vice versa
        """
        self.__status = not self.__status
    def mute(self):
        """
        Changes value of the muted variable if television is on. Saves set volume before changing it to the minimum volume.
        """
        if self.__status == True:
            self.__before = self.__volume
            self.__muted = not self.__muted
            self.__volume = Television.MIN_VOLUME
    def channel_up(self):
        """
        Increases value of channel variable if television is on and variable is not at max value. Sets to minimum value for channel otherwise
        """
        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
    def channel_down(self):
        """
        Decreases value of channel variable if television is on and variable is not a min value. Sets to max value for channel otherwise
        """
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
    def volume_up(self):
        """
        Increases volume if television is on and not muted. If television is muted, unmutes and increases volume. Volume does not change if it is at the max.
        :return:
        """
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.__before
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1
    def volume_down(self):
        """
        Decreases volume if television is on a not muted. If television is muted, unmuted then decreases volume. Volume does not change if it is at the min.
        :return:
        """
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.__before
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1
    def __str__(self):
        """
        :return: Statement reporting state of television's power, channel, and volume
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'