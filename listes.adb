

procedure Listes is 
   
   
   type Element;
   type Liste is access Element;
   type Element is 
      record
	 Info : Integer;
	 Suiv : Liste;
      end record;
   
   
   function Taille_Liste(Li : Liste) return integer is
      Count : Integer
   begin
      
      if Li /= null then
	 Count := 1;
      
      while Li.all.Suiv /= null loop
	 
	 Count := Count +1;
	 Li := Li.all.Suiv;
	 
	 
	 
      end loop;
      
      else
	 Count := 0
	   
      end if;
	 
      return Count;
      
      
   end Taille_Liste;
   
   
   
   procedure Suppr_Multi(Li : Liste) is 
      
      Occu : Tab(
      
   begin
      
      while Li.all.Suiv /= null loop
	 
	 
	 
	 
	 
	 end loop;
      
      
    end Suppr_Multi;
   
   
   
   
   
begin
   
   
   
end Listes
  
