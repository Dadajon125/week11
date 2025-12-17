def parse_settings(config_lines):
        settings = {}
        for line in config_lines:
            try:
            
                parts = line.split(":")
                if len(parts) != 2:
                    raise IndexError
                
                value_name = parts[0]     
                value_int = int(parts[1])

                if value_int < 0 or value_int > 100:
                    raise  ValueError("Out of range")
            
                settings[value_name] = value_int

            except IndexError:
                print(f"Format error in: {line}")
            except ValueError as e:
                print(f"Invalid value in: {line} ({e})")    
            return settings
        
configs = [
    "volume:80",          
    "brightness:120",     
    "difficulty:hard",    
    "mute",               
    "contrast:50"         
]
settings = parse_settings(configs)
print(f"Loaded Settings: {settings}")
            
        


            