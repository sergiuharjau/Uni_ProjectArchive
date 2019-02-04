section .data                           ;Data segment

   star1 db '*', 0x0a   ;new lines 
   lenStar1 equ $-star1
   star2 db '**', 0x0a
   lenStar2 equ $-star2
   star3 db '***', 0x0a
   lenStar3 equ $-star3
   star4 db '****', 0x0a
   lenStar4 equ $-star4
   star5 db '*****', 0x0a 
   lenStar5 equ $-star5
     
   newLine db '0x0a'
   lenNL equ $-newLine 
	
section .text          ;Code Segment
   global _start
	
_start:                ;User prompt
   mov eax, 4
   mov ebx, 1
   mov ecx, star1 
   mov edx, lenStar1 
   int 0x80

   mov eax, 4
   mov ebx, 1
   mov ecx, star2
   mov edx, lenStar2 
   int 0x80

   mov eax, 4
   mov ebx, 1
   mov ecx, star3 
   mov edx, lenStar3 
   int 0x80

   mov eax, 4
   mov ebx, 1
   mov ecx, star4 
   mov edx, lenStar4 
   int 0x80

   mov eax, 4
   mov ebx, 1
   mov ecx, star5 
   mov edx, lenStar5 
   int 0x80

;exit condition 

   mov eax, 1 
   mov ebx, 0 
   int 0x80 
   
   

   
   
   
   
   
   
   
   
   
   
   