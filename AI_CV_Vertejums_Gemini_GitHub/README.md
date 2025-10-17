# AI CV Vērtējuma Projekts (Gemini versija)

Automātiski vērtē, cik labi kandidāta CV atbilst darba aprakstam, izmantojot Google Gemini modeli.

## Lietošana

1. Instalē prasības:
   ```bash
   pip install -r requirements.txt
   ```

2. Izveido `.env` ar savu Google API atslēgu:
   ```
   GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXX
   ```

3. Ieliec failus mapē `sample_inputs/`:
   - `jd.txt` → darba apraksts
   - `cv1.txt`, `cv2.txt` → kandidātu CV

4. Palaid:
   ```bash
   python run_all.py
   ```

5. Rezultāti būs mapē `outputs/`.
