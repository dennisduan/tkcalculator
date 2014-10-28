#!/usr//bin/python

import view
import mockCalBus

if __name__ == '__main__':
    v = view.CalView()
    bus = mockCalBus.CalBus()
    v.setCalBus(bus)
    v.show()

