def mapp(x,in_min,in_max,out_min,out_max):#this function maps a value in one range to the equivalent value in another
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min