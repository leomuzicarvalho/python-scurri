import re


def validate_uk_postcode(postcode):
    """
    Validates UK postcodes according to the format described in Wikipedia.
    
    UK postcode format: A[A]N[A/N] NAA
    Where:
    - A = letter
    - N = number
    - [A/N] = optional letter or number
    - Space separates outward and inward codes
    
    Args:
        postcode (str): The postcode to validate
        
    Returns:
        bool: True if valid UK postcode, False otherwise
    """
    if not postcode or not isinstance(postcode, str):
        return False
    
    # Remove any extra whitespace and convert to uppercase
    postcode = postcode.strip().upper()
    
    # UK postcode regex pattern
    # Format: A[A]N[A/N] NAA
    # Where A = letter, N = number, [A/N] = optional letter or number
    # The outward code can be: A1, AA1, A1A, AA1A, A11, AA11, A1A1, AA1A1
    pattern = r'^(GIR\s?0AA|[A-Z]{1,2}[0-9][0-9A-Z]?(?:[0-9A-Z])?\s?[0-9][A-Z]{2})$'
    
    if not re.match(pattern, postcode):
        return False
    
    # Additional validation rules
    # 1. First character cannot be Q, V, X
    if postcode[0] in ['Q', 'V', 'X']:
        return False
    
    # 2. Second character cannot be I, J, Z (if it exists)
    if len(postcode) > 1 and postcode[1] in ['I', 'J', 'Z']:
        return False
    
    # 3. Third character cannot be I, L, O, Z (if it's a letter)
    if len(postcode) > 2 and postcode[2].isalpha() and postcode[2] in ['I', 'L', 'O', 'Z']:
        return False
    
    # 4. Fourth character cannot be I, L, O, Z (if it's a letter)
    if len(postcode) > 3 and postcode[3].isalpha() and postcode[3] in ['I', 'L', 'O', 'Z']:
        return False
    
    # 5. Last two characters cannot be C, I, K, M, O, V
    if postcode[-2:] in ['CI', 'CK', 'CM', 'CO', 'CV', 'IC', 'IK', 'IM', 'IO', 'IV', 'KC', 'KI', 'KM', 'KO', 'KV', 'MC', 'MI', 'MK', 'MO', 'MV', 'OC', 'OI', 'OK', 'OM', 'OV', 'VC', 'VI', 'VK', 'VM', 'VO', 'VV']:
        return False
    
    return True


def format_uk_postcode(postcode):
    """
    Formats a UK postcode to standard format with proper spacing.
    
    Handles various input formats:
    - "SW1A1AA" -> "SW1A 1AA"
    - "sw1a 1aa" -> "SW1A 1AA"
    - "SW1A  1AA" -> "SW1A 1AA"
    - "SW1A-1AA" -> "SW1A 1AA"
    
    Args:
        postcode (str): The postcode to format
        
    Returns:
        str: Formatted postcode or None if invalid
    """
    if not postcode or not isinstance(postcode, str):
        return None
    
    # Remove all whitespace, hyphens, and convert to uppercase
    postcode = re.sub(r'[\s\-_]+', '', postcode).upper()
    
    # Validate the cleaned postcode
    if not validate_uk_postcode(postcode):
        return None
    
    # Insert space before the last 3 characters
    return f"{postcode[:-3]} {postcode[-3:]}"
