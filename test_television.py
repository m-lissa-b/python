import pytest
from television import Television

class Test:
    def setup_method(self):
        self.tel = Television()

    def teardown_method(self):
        del self.tel

    def test_init(self):
        assert self.tel.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        self.tel.power()
        assert self.tel.__str__() == 'Power = True, Channel = 0, Volume = 0'
        #turn tv back off
        self.tel.power()
        assert self.tel.__str__() == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        #when tv is on, vol +1, then muted
        self.tel.power()
        self.tel.volume_up()
        self.tel.mute()
        assert self.tel.__str__() == 'Power = True, Channel = 0, Volume = 0'

        #when tv is unmuted
        self.tel.mute()
        assert self.tel.__str__() == 'Power = True, Channel = 0, Volume = 1'

        #when tv is off and unmuted
        self.tel.power()
        assert self.tel.__str__() == 'Power = False, Channel = 0, Volume = 1'

        #when tv is off and muted, should not change
        self.tel.mute()
        assert self.tel.__str__() == 'Power = False, Channel = 0, Volume = 1'

    def test_channel_up(self):
        #when tv is off and channel is increased
        self.tel.channel_up()
        assert self.tel.__str__() == 'Power = False, Channel = 0, Volume = 0'

        #when tv is on and channel is increased
        self.tel.power()
        self.tel.channel_up()
        assert self.tel.__str__() == 'Power = True, Channel = 1, Volume = 0'

        #when tv is on and channel reaches max
        self.tel.channel_up()
        self.tel.channel_up()
        self.tel.channel_up()
        assert self.tel.__str__() == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        #tv is off, channel decreased
        self.tel.channel_down()
        assert self.tel.__str__() == 'Power = False, Channel = 0, Volume = 0'

        #tv is on, channel decreased below min
        self.tel.power()
        self.tel.channel_down()
        assert self.tel.__str__() == 'Power = True, Channel = 3, Volume = 0'

    def test_volume_up(self):
        #tv is off, volume is increased
        self.tel.volume_up()
        assert self.tel.__str__() == 'Power = False, Channel = 0, Volume = 0'

        #tv is on, volume is increased
        self.tel.power()
        self.tel.volume_up()
        assert self.tel.__str__() == 'Power = True, Channel = 0, Volume = 1'

        #tv on, muted, volume increased
        self.tel.mute()
        self.tel.volume_up()
        assert self.tel.__str__() == 'Power = True, Channel = 0, Volume = 2'

        #tv is on, volume past max
        self.tel.volume_up()
        self.tel.volume_up()
        assert self.tel.__str__() == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        #tv is off, volume decreased
        self.tel.volume_down()
        assert self.tel.__str__() == 'Power = False, Channel = 0, Volume = 0'

        #tv is on, volume increased to max then decreased by 1
        self.tel.power()
        self.tel.volume_up()
        self.tel.volume_up()
        self.tel.volume_down()
        assert self.tel.__str__() == 'Power = True, Channel = 0, Volume = 1'

        #tv on, muted, volume lowered
        self.tel.mute()
        self.tel.volume_down()
        assert self.tel.__str__() == 'Power = True, Channel = 0, Volume = 0'

        #decrease volume past min
        self.tel.volume_down()
        assert self.tel.__str__() == 'Power = True, Channel = 0, Volume = 0'

