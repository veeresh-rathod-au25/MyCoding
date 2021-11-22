def trap(self, height: List[int]) -> int:
        
  lp = 0
  rp = len(height) - 1
  max_left, max_right, water = 0, 0, 0
  
  while lp <= rp:
      
      if height[lp] <= height[rp]:
          if max_left > height[lp]:
              water += max_left - height[lp]
          else:
              max_left = height[lp]
          
          lp += 1
      else:
          if max_right > height[rp]:
              water += max_right - height[rp]
          else:
              max_right = height[rp]
          
          rp -= 1
          
  return water