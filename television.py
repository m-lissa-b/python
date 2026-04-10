class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3
    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.min_volume
        self.__channel = Television.min_channel
        self.__before = Television.min_volume


    def power(self):
        self.__status = not self.__status
    def mute(self):
        if self.__status == True:
            self.__before = self.__volume
            self.__muted = not self.__muted
            self.__volume = Television.min_volume
    def channel_up(self):
        if self.__status == True:
            if self.__channel == Television.max_channel:
                self.__channel = Television.min_channel
            else:
                self.__channel += 1
    def channel_down(self):
        if self.__status == True:
            if self.__channel == Television.min_channel:
                self.__channel = Television.max_channel
            else:
                self.__channel -= 1
    def volume_up(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.__before
            if self.__volume == Television.max_volume:
                pass
            else:
                self.__volume += 1
    def volume_down(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.__before
            if self.__volume == Television.min_volume:
                pass
            else:
                self.__volume -= 1
    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'