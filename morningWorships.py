from bs4 import BeautifulSoup
import pandas as pd
import re

def extract_video_info(div):
    title = div.find('h3').text.strip()
    url = div.find('a')['href']
    return title, url

def get_video_code(url):
    match = re.search(r"pub-(.+)_VIDEO", url)
    if match:
        return match.group(1)
    return None

def scrape_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    divs = soup.find_all('div', class_='synopsis')

    print(len(divs))

    video_info = []
    for div in divs:
        url = div.find('a')['href']
        code = get_video_code(url)
        if code:
            video_info.append((code, *extract_video_info(div)))

    return video_info

def generate_excel(video_info_spanish, video_info_english):
    df_spanish = pd.DataFrame(video_info_spanish, columns=['Code', 'Spanish Title', 'Spanish URL'])
    df_english = pd.DataFrame(video_info_english, columns=['Code', 'English Title', 'English URL'])

    # Merge data frames on video code
    df = pd.merge(df_spanish, df_english, on='Code', how='outer')

    # Fill NaN values with empty strings
    df = df.fillna('')

    # Save to Excel
    df.to_excel('MorningWorships.xlsx', index=False)

if __name__ == "__main__":
    # Paste the HTML source code here
    spanish_html = """
    <div class="synopsisGroup">

         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_19_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_19_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:08</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_19_VIDEO" class="jsNoScroll">Gary Breaux: Cómo protegernos de la información falsa (Dan. 11:27)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_18_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_18_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:03</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_18_VIDEO" class="jsNoScroll">Geoffrey Jackson: Transfórmese, no se disfrace (Rom. 12:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-111_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-111/univ/art/jwb-111_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">11:08</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-111_6_VIDEO" class="jsNoScroll">Harold Corkern: No dejemos que Satanás se aproveche de nosotros (2 Cor. 2:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_17_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_17_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:53</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_17_VIDEO" class="jsNoScroll">Troy Snyder: Ayuda para los desanimados (Sal. 34:18)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_16_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_16_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:25</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_16_VIDEO" class="jsNoScroll">Clive Martin: Demos servicio sagrado con temor de Dios (Sal. 86:11, 12)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_15_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_15_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:23</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_15_VIDEO" class="jsNoScroll">Leonard Myers: Jehová recompensa a sus siervos fieles (Heb. 11:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:39</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_14_VIDEO" class="jsNoScroll">Mark Noumair: Jehová está con ellos (Zac. 8:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-110_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-110/univ/art/jwb-110_univ_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:45</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-110_7_VIDEO" class="jsNoScroll">Mark Sanderson: La paz que ningún ser humano puede entender (Filip. 4:6, 7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">29:11</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_1_VIDEO" class="jsNoScroll">Adoración matutina para el día de la Conmemoración del 2024. Kenneth Cook: Lo que debemos recordar de Jesús (Luc. 22:19)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:52</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_12_VIDEO" class="jsNoScroll">Robert Luccioni: “¿Crees tú esto?” (Juan 11:26)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:07</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_13_VIDEO" class="jsNoScroll">James Mantz: Evitemos la trampa de la codicia (Col. 3:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:54</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_10_VIDEO" class="jsNoScroll">Gage Fleegle: Las prohibiciones son para nuestro bien (Ecl. 7:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_9_VIDEO" class="jsNoScroll">Jonathan Smith: Vea el cuadro completo (1 Sam. 17:42)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-099_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-099/univ/art/jwb-099_univ_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-099_7_VIDEO" class="jsNoScroll">Seth Hyatt: Nos ven como farsantes, aunque decimos la verdad (2 Cor. 6:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:13</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_8_VIDEO" class="jsNoScroll">Kenneth Godburn: Escuchemos con apacibilidad (Sant. 1:19-21)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:04</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_7_VIDEO" class="jsNoScroll">Donald Gordon: Presta constante atención a tu enseñanza (1 Tim. 4:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:14</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_6_VIDEO" class="jsNoScroll">Nicholas Ahladis: Jehová se preocupa por los “pequeños” (Mat. 18:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_5_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_05_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:58</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_5_VIDEO" class="jsNoScroll">Robert Ciranko: ¿Qué significa ser un amigo verdadero? (Mat. 7:12)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_4_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_04_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:50</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_4_VIDEO" class="jsNoScroll">Kenneth Flodin: Aprendamos de nuestros errores (Filip. 3:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:46</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_3_VIDEO" class="jsNoScroll">Geoffrey Jackson: Demos honra a las autoridades superiores (Rom. 13:7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-107_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-107/univ/art/jwb-107_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:06</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-107_12_VIDEO" class="jsNoScroll">John Ekrann: ¿Cómo resolver malentendidos? (Hech. 15:37-39)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-107_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-107/univ/art/jwb-107_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:03</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-107_11_VIDEO" class="jsNoScroll">Stephen Lett: Ayudemos a los jóvenes a progresar (Mar. 10:13, 14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-108_16_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-108/univ/art/jwb-108_univ_lss_16_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:07</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-108_16_VIDEO" class="jsNoScroll">Leonard Myers: La transfiguración fortalece nuestra fe (2 Ped. 1:19)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-108_15_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-108/univ/art/jwb-108_univ_lss_15_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:12</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-108_15_VIDEO" class="jsNoScroll">Anthony Griffin: La manera en que Jehová nos trata nos ayuda a recuperar las fuerzas (Deut. 32:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-108_17_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-108/univ/art/jwb-108_univ_lss_17_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-108_17_VIDEO" class="jsNoScroll">William Malenfant: Elihú escuchó con paciencia (Sant. 1:19)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-108_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-108/univ/art/jwb-108_univ_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:59</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-108_14_VIDEO" class="jsNoScroll">Jeffrey Winder: Ser modestos beneficia a los demás (Mat. 22:39)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-106_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-106/univ/art/jwb-106_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:03</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-106_11_VIDEO" class="jsNoScroll">Clive Martin: Imitemos la humildad del Gran Pastor (Sal. 18:35)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-106_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-106/univ/art/jwb-106_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:48</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-106_10_VIDEO" class="jsNoScroll">Paul Gillies: Reflejemos la personalidad de Jehová siguiendo el modelo de Jesús (Efes. 4:20, 21)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-106_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-106/univ/art/jwb-106_univ_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:18</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-106_3_VIDEO" class="jsNoScroll">Geoffrey Jackson: Cómo crear oportunidades de predicarle a la gente (Juan 4:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-106_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-106/univ/art/jwb-106_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:12</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-106_9_VIDEO" class="jsNoScroll">Joel Dellinger: Entender las profecías nos motiva a actuar (Apoc. 7:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-105_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-105/univ/art/jwb-105_univ_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:42</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-105_8_VIDEO" class="jsNoScroll">Harold Corkern: Imitemos a Dios valorando a los demás (Heb. 6:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-102/univ/art/jwb-102_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:31</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_11_VIDEO" class="jsNoScroll">Gage Fleegle: El espíritu santo, un valioso regalo de Jehová (Juan 3:34)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-102/univ/art/jwb-102_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:01</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_10_VIDEO" class="jsNoScroll">David Schafer: “Confía en Jehová y haz el bien” (Sal. 37:3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-102/univ/art/jwb-102_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:05</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_6_VIDEO" class="jsNoScroll">William Turner : ¿Qué nos hace valiosos para Jehová? (1 Ped. 3:4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-102/univ/art/jwb-102_univ_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:29</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_8_VIDEO" class="jsNoScroll">Gajus Glockentin: Tengamos cuidado con la satisfacción inmediata (Tito 2:12)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-102/univ/art/jwb-102_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:25</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_9_VIDEO" class="jsNoScroll">Robert Luccioni: Hagamos las cosas como Jehová quiere (Juan 5:19)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-101/univ/art/jwb-101_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:55</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_12_VIDEO" class="jsNoScroll">Hermanus van Selm: Jehová cuida a los humildes (Is. 57:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-101/univ/art/jwb-101_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:16</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_11_VIDEO" class="jsNoScroll">John Ekrann: "Amantes del dinero" (2 Tim. 3:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_5_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-101/univ/art/jwb-101_univ_lss_05_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:05</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_5_VIDEO" class="jsNoScroll">Geoffrey Jackson: Las cualidades de un buen maestro (1 Tes. 2:7, 8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-101/univ/art/jwb-101_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:35</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_9_VIDEO" class="jsNoScroll">Mark Noumair: Jehová anima a sus siervos (Jer. 15:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-101/univ/art/jwb-101_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:17</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_10_VIDEO" class="jsNoScroll">Seth Hyatt: Veamos el matrimonio como lo ve Jehová (Mat. 19:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-105_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-105/univ/art/jwb-105_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:52</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-105_9_VIDEO" class="jsNoScroll">Christopher Mavor: Averigüemos cuáles son nuestros motivos (Prov. 16:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-099_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-099/univ/art/jwb-099_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:33</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-099_12_VIDEO" class="jsNoScroll">Ronald Curzan: Vivamos juntos en unidad (Sal. 133:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-105_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-105/univ/art/jwb-105_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:43</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-105_12_VIDEO" class="jsNoScroll">David Splane: Demos consejos con espíritu apacible (Gál. 6:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-099_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-099/univ/art/jwb-099_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:44</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-099_11_VIDEO" class="jsNoScroll">Robert Ciranko: Jehová es quien nos disciplina (1 Cor. 5:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-099_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-099/univ/art/jwb-099_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:38</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-099_10_VIDEO" class="jsNoScroll">Gary Breaux: Preparemos nuestro corazón para orar (Esd. 7:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-104_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-104/univ/art/jwb-104_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:44</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-104_11_VIDEO" class="jsNoScroll">Leonard Myers: Mostremos amor a nuestros familiares no Testigos sin dejar de ser leales a Jehová (Mat. 10:34, 35)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-104_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-104/univ/art/jwb-104_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-104_10_VIDEO" class="jsNoScroll">Alex Reinmueller: ¡Sigamos luchando contra el pecado! (Rom. 7:22, 23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-096/univ/art/jwb-096_univ_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:50</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_14_VIDEO" class="jsNoScroll">Baltasar Perla: Nunca dejemos de ser humildes (1 Ped. 5:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-096/univ/art/jwb-096_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:17</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_13_VIDEO" class="jsNoScroll">David Splane: “Toda la Escritura está inspirada por Dios” (2 Tim. 3:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-096/univ/art/jwb-096_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:06</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_6_VIDEO" class="jsNoScroll">Stephen Lett: Nunca dejen que Satanás los intimide (Deut. 1:17)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-096/univ/art/jwb-096_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:48</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_12_VIDEO" class="jsNoScroll">Joel Dellinger: “Alégrense siempre a causa del Señor” (Filip. 4:4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-096/univ/art/jwb-096_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:49</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_11_VIDEO" class="jsNoScroll">William Malenfant: Diferencias entre el hombre físico y el hombre espiritual (1 Cor. 2:12-15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-095_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-095/univ/art/jwb-095_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:55</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-095_12_VIDEO" class="jsNoScroll">Seth Hyatt: Mostremos misericordia (Luc. 10:37)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-095_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-095/univ/art/jwb-095_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:49</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-095_11_VIDEO" class="jsNoScroll">Patrick LaFranca: Adquiramos sabiduría día tras día (Prov. 3:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-095_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-095/univ/art/jwb-095_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:51</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-095_6_VIDEO" class="jsNoScroll">Robert Luccioni: Seamos como Gedeón (Efes. 4:1, 2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-095_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-095/univ/art/jwb-095_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:52</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-095_10_VIDEO" class="jsNoScroll">Kenneth Flodin: El yugo de Jesús es fácil de llevar (Mat. 11:29, 30)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-092/univ/art/jwb-092_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">26:46</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_10_VIDEO" class="jsNoScroll">Adoración matutina para el día de la Conmemoración. Samuel Herd: “Sigan haciendo esto en memoria de mí” una vez al año (Luc. 22:19)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-092/univ/art/jwb-092_univ_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:08</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_14_VIDEO" class="jsNoScroll">Kenneth Cook: No nos dejemos engañar, apoyemos el Reino de Dios (Jer. 10:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-092/univ/art/jwb-092_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:18</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_13_VIDEO" class="jsNoScroll">Izak Marais: Usemos siempre palabras agradables (Col. 4:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-092/univ/art/jwb-092_univ_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:32</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_7_VIDEO" class="jsNoScroll">David Schafer: Digamos palabras de ánimo (Hech. 13:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-092/univ/art/jwb-092_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:43</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_11_VIDEO" class="jsNoScroll">John Ekrann: Fortalezcamos nuestra fe en la resurrección (Hech. 9:40)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-092/univ/art/jwb-092_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_12_VIDEO" class="jsNoScroll">Gajus Glockentin: Meditar en el rescate protege nuestra valiosa unidad (Juan 10:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-103_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-103/univ/art/jwb-103_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:26</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-103_13_VIDEO" class="jsNoScroll">James Mantz: “Hagan amigos usando las riquezas injustas” (Luc. 16:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-103_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-103/univ/art/jwb-103_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:55</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-103_12_VIDEO" class="jsNoScroll">Stephen Lett: Cuidado, el materialismo es peligroso (Mat. 6:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-103_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-103/univ/art/jwb-103_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:02</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-103_11_VIDEO" class="jsNoScroll">Mark Noumair: "¡No llegará tarde!" (Hab. 2:3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-103_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-103/univ/art/jwb-103_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">11:00</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-103_10_VIDEO" class="jsNoScroll">Ronald Curzan: Seamos un amigo verdadero (Prov. 17:17)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-100_19_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-100/univ/art/jwb-100_univ_lss_19_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-100_19_VIDEO" class="jsNoScroll">Christopher Mavor: Acerquémonos a Dios mediante la oración (Efes. 6:18)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-100_18_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-100/univ/art/jwb-100_univ_lss_18_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:52</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-100_18_VIDEO" class="jsNoScroll">Hermanus van Selm: La compasión y el rescate (1 Juan 4:9-11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-100_20_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-100/univ/art/jwb-100_univ_lss_20_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:00</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-100_20_VIDEO" class="jsNoScroll">Clive Martin: Imitemos la fe de Sara (Heb. 11:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-100_17_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-100/univ/art/jwb-100_univ_lss_17_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:25</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-100_17_VIDEO" class="jsNoScroll">Gary Breaux: Los ancianos y las autoridades superiores, cada uno en su debido lugar (Rom. 13:1-4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-098_15_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-098/univ/art/jwb-098_univ_lss_15_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:18</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-098_15_VIDEO" class="jsNoScroll">Seth Hyatt: Demos "fruto con aguante" a pesar de las pruebas (Luc. 8:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-098_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-098/univ/art/jwb-098_univ_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:20</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-098_14_VIDEO" class="jsNoScroll">Geoffrey Jackson: “Los mansos heredarán la tierra” (Sal. 37:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-094_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-094/univ/art/jwb-094_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:59</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-094_13_VIDEO" class="jsNoScroll">Robert Luccioni: Estemos atentos a nuestra actitud para no volvernos traidores (Mal. 2:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-094_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-094/univ/art/jwb-094_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:13</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-094_12_VIDEO" class="jsNoScroll">Kenneth Flodin: Hagamos el bien y compartamos lo que tenemos (Heb. 13:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-094_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-094/univ/art/jwb-094_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:00</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-094_6_VIDEO" class="jsNoScroll">David Splane: “Protege tu corazón” (Prov. 4:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-094_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-094/univ/art/jwb-094_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:12</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-094_11_VIDEO" class="jsNoScroll">Joel Dellinger: El día de Jehová “no llegará tarde” (Hab. 2:3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-093/univ/art/jwb-093_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:52</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_13_VIDEO" class="jsNoScroll">Mark Sanderson: Fueron intachables (1 Rey. 15:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-093/univ/art/jwb-093_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:46</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_12_VIDEO" class="jsNoScroll">Ronald Curzan: Agradezcamos todo lo que Jehová ha hecho por nosotros (Sal. 116:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-093/univ/art/jwb-093_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:03</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_11_VIDEO" class="jsNoScroll">John Ekrann: No exijamos más de lo que Jehová pide y sigamos el orden teocrático (Hech. 15:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-093/univ/art/jwb-093_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:17</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_10_VIDEO" class="jsNoScroll">Samuel Herd: “Recibí una espina en la carne” (2 Cor. 12:7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-093/univ/art/jwb-093_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:10</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_6_VIDEO" class="jsNoScroll">William Turner: Seamos imparciales (Juan 4:31)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-090_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-090/univ/art/jwb-090_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:21</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-090_13_VIDEO" class="jsNoScroll">Gajus Glockentin: “Hagan amigos usando las riquezas injustas” (Luc. 16:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-090_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-090/univ/art/jwb-090_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:46</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-090_10_VIDEO" class="jsNoScroll">David Schafer: Vivimos en la temporada de la cosecha (Mat. 9:37)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-090_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-090/univ/art/jwb-090_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:47</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-090_12_VIDEO" class="jsNoScroll">Izak Marais: Aceptemos de buena gana la disciplina de Jehová (Heb. 12:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-090_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-090/univ/art/jwb-090_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:41</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-090_11_VIDEO" class="jsNoScroll">Kenneth Cook: “Aférrense a lo que tienen hasta que yo venga” (Apoc. 2:25)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-091_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-091/univ/art/jwb-091_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:41</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-091_6_VIDEO" class="jsNoScroll">Christopher Mavor: Jehová ama a su pueblo (Is. 54:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-091_5_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-091/univ/art/jwb-091_univ_lss_05_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:13</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-091_5_VIDEO" class="jsNoScroll">Geoffrey Jackson: Llevemos “el cinturón de la verdad” siempre bien ajustado (Efes. 6:14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-089_15_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-089/univ/art/jwb-089_univ_lss_15_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:40</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-089_15_VIDEO" class="jsNoScroll">Leon Weaver: Las circunstancias cambian, no dejemos de predicar (Hech. 16:26-31)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-089_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-089/univ/art/jwb-089_univ_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-089_14_VIDEO" class="jsNoScroll">Kenneth Flodin: La mansedumbre, una cualidad compleja (Núm. 12:3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-089_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-089/univ/art/jwb-089_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:48</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-089_12_VIDEO" class="jsNoScroll">Gary Breaux: Las historias, un método de enseñanza muy eficaz (1 Juan 5:19)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-089_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-089/univ/art/jwb-089_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:39</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-089_13_VIDEO" class="jsNoScroll">Clive Martin: ¿Qué busca Jehová en nosotros? (Prov. 27:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-088/univ/art/jwb-088_univ_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:31</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_14_VIDEO" class="jsNoScroll">Seth Hyatt: Elijamos “la mejor parte” (Luc. 10:42)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-088/univ/art/jwb-088_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:43</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_13_VIDEO" class="jsNoScroll">Joel Dellinger: Su liberación se acerca (Apoc. 6:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-088/univ/art/jwb-088_univ_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_7_VIDEO" class="jsNoScroll">William Malenfant: Jóvenes que quieren a Jehová (Prov. 20:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-088/univ/art/jwb-088_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:34</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_12_VIDEO" class="jsNoScroll">Hermanus van Selm: Grabemos en nuestro corazón los pensamientos de Jehová (Sal. 119:97)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-088/univ/art/jwb-088_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:58</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_10_VIDEO" class="jsNoScroll">Mark Noumair: Estemos preparados para la persecución (1 Ped. 4:4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-088/univ/art/jwb-088_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">16:55</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_9_VIDEO" class="jsNoScroll">Adoración matutina para el día de la Conmemoración. Gerrit Lösch: Jehová hará que se cumpla su propósito (Gén. 2:15-17)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-087_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-087/univ/art/jwb-087_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:08</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-087_12_VIDEO" class="jsNoScroll">Patrick LaFranca: “Acuérdate de tu Gran Creador” (Ecl. 12:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-087_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-087/univ/art/jwb-087_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:34</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-087_11_VIDEO" class="jsNoScroll">Robert Luccioni: “No se olviden de mostrar hospitalidad” (Heb. 13:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-087_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-087/univ/art/jwb-087_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">11:04</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-087_10_VIDEO" class="jsNoScroll">Harold Corkern: “Compra la verdad y nunca la vendas” (Prov. 23:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-097_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-097/univ/art/jwb-097_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:00</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-097_13_VIDEO" class="jsNoScroll">John Ekrann: Seamos amables y cariñosos (1 Tes. 2:7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-097_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-097/univ/art/jwb-097_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:12</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-097_12_VIDEO" class="jsNoScroll">Kenneth Cook: El sacrificio vale la pena (Mar. 10:29, 30)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-097_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-097/univ/art/jwb-097_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:43</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-097_11_VIDEO" class="jsNoScroll">David Schafer: “Dedícate de lleno a ellas” (1 Tim. 4:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-097_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-097/univ/art/jwb-097_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:23</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-097_10_VIDEO" class="jsNoScroll">James Mantz: Jehová nos da libertad verdadera (2 Cor. 3:17)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-086_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-086/univ/art/jwb-086_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:26</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-086_10_VIDEO" class="jsNoScroll">Izak Marais: Esperemos con paciencia a que Jehová actúe (Hab. 2:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-086_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-086/univ/art/jwb-086_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-086_9_VIDEO" class="jsNoScroll">Leonard Myers: Estemos pendientes de la proclamación de “paz y seguridad” (1 Tes. 5:3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-086_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-086/univ/art/jwb-086_univ_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:19</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-086_2_VIDEO" class="jsNoScroll">William Malenfant: Satanás es “el padre de la mentira” (Juan 8:44)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-086_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-086/univ/art/jwb-086_univ_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:42</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-086_8_VIDEO" class="jsNoScroll">Ronald Curzan: “Serán una sola carne” (Gén. 2:24)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-085_16_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-085/univ/art/jwb-085_univ_lss_16_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:59</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-085_16_VIDEO" class="jsNoScroll">Robert Luccioni: “Sigo adelante hacia la meta” (Filip. 3:14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-085_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-085/univ/art/jwb-085_univ_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:37</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-085_2_VIDEO" class="jsNoScroll">Geoffrey Jackson: Se ayuda económicamente a los hermanos (Prov. 19:17)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-084_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-084/univ/art/jwb-084_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-084_10_VIDEO" class="jsNoScroll">Mark Noumair: Sigamos en las manos del Alfarero (Jos. 1:1, 2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-084_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-084/univ/art/jwb-084_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:43</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-084_9_VIDEO" class="jsNoScroll">Stephen Lett: Aprovechemos "el poder que va más allá de lo normal" (2 Cor. 4:7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-084_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-084/univ/art/jwb-084_univ_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:21</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-084_7_VIDEO" class="jsNoScroll">Gajus Glockentin: Qué es la resiliencia y cómo se consigue (Luc. 10:39)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-083_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-083/univ/art/jwb-083_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:58</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-083_10_VIDEO" class="jsNoScroll">Hermanus van Selm: La obediencia nos protege (2 Tes. 1:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-083_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-083/univ/art/jwb-083_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:30</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-083_11_VIDEO" class="jsNoScroll">Mark Sanderson: “Mi paz les doy” (Juan 14:27)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-083_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-083/univ/art/jwb-083_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-083_6_VIDEO" class="jsNoScroll">William Turner: Consuele y fortalezca a los hermanos (2 Tes. 2:16, 17)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-082_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-082/univ/art/jwb-082_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-082_10_VIDEO" class="jsNoScroll">Geoffrey Jackson: Seamos fieles al usar las riquezas (Luc. 16:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-082_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-082/univ/art/jwb-082_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:20</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-082_9_VIDEO" class="jsNoScroll">Kenneth Flodin: “Los planes del que es trabajador” (Prov. 21:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-081_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-081/univ/art/jwb-081_univ_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:51</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-081_2_VIDEO" class="jsNoScroll">Stephen Lett: Veamos el cuadro completo (Hech. 8:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-080_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-080/univ/art/jwb-080_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:25</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-080_13_VIDEO" class="jsNoScroll">Hermanus van Selm: ¡Ánimo! ¡Sean valientes! (Juan 16:33)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-080_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-080/univ/art/jwb-080_univ_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:40</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-080_7_VIDEO" class="jsNoScroll">David Splane: Las profecías de nuestro Dios nunca fallan (Sal. 46:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-080_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-080/univ/art/jwb-080_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:55</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb-080_12_VIDEO" class="jsNoScroll">Gajus Glockentin: ¿Por qué esforzarnos por progresar? (1 Tim. 3:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202104_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202104/univ/art/jwb_univ_202104_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:10</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202104_7_VIDEO" class="jsNoScroll">Gary Breaux: Permitamos que Jehová nos moldee (Is. 64:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202104_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202104/art/jwb_univ_202104_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:43</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202104_9_VIDEO" class="jsNoScroll">William Turner: “Jehová levanta a los mansos” (Sal. 147:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202103_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202103/art/jwb_univ_202103_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:21</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202103_12_VIDEO" class="jsNoScroll">Izak Marais: “Den muerte a los miembros de su cuerpo” (Col. 3:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202103_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202103/art/jwb_univ_202103_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">26:10</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202103_13_VIDEO" class="jsNoScroll">Adoración matutina para el día de la Conmemoración. Stephen Lett: “El espíritu mismo da testimonio con nuestro espíritu” (Rom. 8:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202103_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202103/univ/art/jwb_univ_202103_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:21</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202103_8_VIDEO" class="jsNoScroll">Robert Ciranko: “Serán una sola carne” (Gén. 2:24)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202103_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202103/art/jwb_univ_202103_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202103_9_VIDEO" class="jsNoScroll">Geoffrey Jackson: Sigan transformándose (Rom. 12:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202102_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202102/art/jwb_univ_202102_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">12:00</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202102_12_VIDEO" class="jsNoScroll">Mark Sanderson: Mantengan la misma actitud mental que tuvo Cristo (Filip. 2:5, 7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202102_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202102/art/jwb_univ_202102_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:23</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202102_11_VIDEO" class="jsNoScroll">Mark Noumair: “Esdras había preparado su corazón” (Esd. 7:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202102_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202102/art/jwb_univ_202102_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:21</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202102_10_VIDEO" class="jsNoScroll">Alex Reinmueller: "Jehová nuestro Dios es un solo Jehová" (Deut. 6:4, 5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202101_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202101/art/jwb_univ_202101_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:01</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202101_13_VIDEO" class="jsNoScroll">James Mantz: “No te enojes fácilmente” (Ecl. 7:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202101_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202101/univ/art/jwb_univ_202101_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:15</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202101_12_VIDEO" class="jsNoScroll">Joel Dellinger: “La fe es la certeza de que sucederá” (Heb. 11:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202012_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202012/art/jwb_univ_202012_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:36</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202012_11_VIDEO" class="jsNoScroll">Leonard Myers: Preocupémonos unos por otros (1 Cor. 12:25)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202012_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202012/art/jwb_univ_202012_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:04</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202012_6_VIDEO" class="jsNoScroll">William Malenfant: ¿Estás aprendiendo un nuevo idioma? (Neh. 13:24)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202012_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202012/art/jwb_univ_202012_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202012_9_VIDEO" class="jsNoScroll">Mark Noumair: La predicación vence a Satanás (Apoc. 12:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202011_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202011/art/jwb_univ_202011_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:09</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202011_11_VIDEO" class="jsNoScroll">Robert Luccioni: Fortalezcamos nuestro tronco espiritual (2 Tim. 3:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202011_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202011/art/jwb_univ_202011_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:36</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202011_7_VIDEO" class="jsNoScroll">Joel Dellinger: Aprovechemos al máximo la enseñanza de Jehová (Prov. 3:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202011_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202011/art/jwb_univ_202011_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:53</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202011_9_VIDEO" class="jsNoScroll">Ronald Curzan: Tenemos la esperanza de la resurrección (Hech. 24:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202010_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202010/art/jwb_univ_202010_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:50</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202010_12_VIDEO" class="jsNoScroll">Gene Smalley: ¿Perdonamos a los demás? (Luc. 18:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202010_16_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202010/art/jwb_univ_202010_lss_16_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:11</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202010_16_VIDEO" class="jsNoScroll">Robert Luccioni: Un momento conveniente para tentarnos (Luc. 4:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202010_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202010/art/jwb_univ_202010_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:52</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202010_6_VIDEO" class="jsNoScroll">Harold Corkern: Firmes contra el enemigo (1 Ped. 5:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202010_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202010/art/jwb_univ_202010_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:41</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202010_9_VIDEO" class="jsNoScroll">Stephen Lett: “Acérquense a Dios” (Sant. 4:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202009_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202009/art/jwb_univ_202009_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:26</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202009_8_VIDEO" class="jsNoScroll">William Turner: Demos a conocer “las buenas noticias” (Rom. 1:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202009_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202009/art/jwb_univ_202009_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:33</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202009_10_VIDEO" class="jsNoScroll">Mark Sanderson: “La sabiduría está con los modestos” (Prov. 11:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202007_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202007/art/jwb_univ_202007_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:35</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202007_11_VIDEO" class="jsNoScroll">Ralph Walls: “Reflexiona sobre estas cosas” (1 Tim. 4:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202007_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202007/art/jwb_univ_202007_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:37</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202007_10_VIDEO" class="jsNoScroll">Gajus Glockentin: Protejámonos de las mentiras (Col. 3:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202006_5_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202006/art/jwb_univ_202006_lss_05_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:38</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202006_5_VIDEO" class="jsNoScroll">Leonard Myers: Seamos razonables en la familia (Col. 3:18-20)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202006_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202006/art/jwb_univ_202006_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:17</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202006_2_VIDEO" class="jsNoScroll">Alex Reinmueller: Seamos leales cuando se nos juzgue mal (1 Sam. 20:30)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202005_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202005/art/jwb_univ_202005_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:06</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202005_11_VIDEO" class="jsNoScroll">David Schafer: Aprendamos a estar contentos con lo que tenemos (Heb. 13:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202005_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202005/art/jwb_univ_202005_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:35</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202005_14_VIDEO" class="jsNoScroll">Mark Sanderson: Busquemos el beneficio de los demás (1 Cor. 10:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202005_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202005/art/jwb_univ_202005_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:42</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202005_9_VIDEO" class="jsNoScroll">William Malenfant: “Formarán un solo rebaño” (Juan 10:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202004/univ/art/jwb_univ_202004_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:58</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_14_VIDEO" class="jsNoScroll">Joel Dellinger: Sigamos adelante con fe, no con miedo (Is. 41:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202004/univ/art/jwb_univ_202004_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:07</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_12_VIDEO" class="jsNoScroll">Robert Ciranko: Cuidado con el coqueteo y el ego (1 Tim. 5:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202004/art/jwb_univ_202004_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_7_VIDEO" class="jsNoScroll">John Ekrann: ¿Vemos la mano de Jehová? (Is. 66:14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202004/univ/art/jwb_univ_202004_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:12</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_10_VIDEO" class="jsNoScroll">Harold Corkern: Jehová es “el Dios de todo consuelo” (2 Cor. 1:3, 4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202004/univ/art/jwb_univ_202004_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:14</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_13_VIDEO" class="jsNoScroll">Robert Luccioni: Pensemos como piensa Dios, no como piensa el hombre (Mat. 16:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202004/art/jwb_univ_202004_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">22:47</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_9_VIDEO" class="jsNoScroll">Geoffrey Jackson: “Cristo murió por nosotros” (Rom. 5:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202003_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202003/art/jwb_univ_202003_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:48</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202003_12_VIDEO" class="jsNoScroll">Robert Luccioni: “La fuente de agua viva” (Jer. 2:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202003_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202003/art/jwb_univ_202003_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:54</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202003_14_VIDEO" class="jsNoScroll">John Ekrann: Seamos como barro en las manos de Jehová (Rom. 12:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202002_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202002/univ/art/jwb_univ_202002_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:11</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202002_11_VIDEO" class="jsNoScroll">Hermanus van Selm: Seamos fieles como Noé (Gén. 6:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202002_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202002/art/jwb_univ_202002_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">11:27</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202002_7_VIDEO" class="jsNoScroll">Stephen Lett: Evitemos todo tipo de codicia (Jer. 45:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202002_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202002/art/jwb_univ_202002_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:19</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202002_9_VIDEO" class="jsNoScroll">Ronald Curzan: Que el nombre de Jehová sea santificado (Mat. 6:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202001_26_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202001/univ/art/jwb_univ_202001_lss_26_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:46</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202001_26_VIDEO" class="jsNoScroll">David Schafer: Imitemos la generosidad de Jehová (1 Crón. 29:14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202001_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202001/univ/art/jwb_univ_202001_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:16</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202001_2_VIDEO" class="jsNoScroll">David Splane: La esperanza de la resurrección (Heb. 11:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201912_4_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201912/art/jwb_univ_201912_lss_04_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:32</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201912_4_VIDEO" class="jsNoScroll">Patrick LaFranca: “Acuérdense de los que los dirigen” (Heb. 13:7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201911_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201911/art/jwb_univ_201911_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:26</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201911_12_VIDEO" class="jsNoScroll">Gary Breaux: Respetemos a Jehová profundamente (Jos. 9:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201911_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201911/art/jwb_univ_201911_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:14</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201911_10_VIDEO" class="jsNoScroll">James Mantz: Jehová es nuestro Alfarero (Is. 64:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201910_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201910/univ/art/jwb_univ_201910_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:16</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201910_10_VIDEO" class="jsNoScroll">Stephen Lett: No seamos murmuradores (Sant. 3:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201910_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201910/univ/art/jwb_univ_201910_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:45</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201910_8_VIDEO" class="jsNoScroll">Robert Ciranko: Identifiquemos las mentiras de Satanás (Gén. 3:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201909_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201909/univ/art/jwb_univ_201909_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:18</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201909_9_VIDEO" class="jsNoScroll">Geoffrey Jackson: “Háganlo todo para la gloria de Dios” (1 Cor. 10:31)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201909_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201909/art/jwb_univ_201909_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:18</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201909_7_VIDEO" class="jsNoScroll">Gajus Glockentin: “Opónganse al Diablo” (Sant. 4:7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201908_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201908/univ/art/jwb_univ_201908_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:06</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201908_9_VIDEO" class="jsNoScroll">David Schafer: Toda palabra que sale de la boca de Jehová (Mat. 4:4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201907_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201907/art/jwb_univ_201907_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:35</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201907_9_VIDEO" class="jsNoScroll">Alex Reinmueller: Veamos con equilibrio los sentimientos de culpa (2 Sam. 12:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201905_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201905/art/jwb_univ_201905_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:56</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201905_13_VIDEO" class="jsNoScroll">Stephen Lett: Sigamos tras el amor (1 Juan 3:18)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201905_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201905/art/jwb_univ_201905_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:10</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201905_9_VIDEO" class="jsNoScroll">William Turner: Lo que nos hace felices de verdad (Mat. 5:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201904_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201904/art/jwb_univ_201904_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:17</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201904_12_VIDEO" class="jsNoScroll">Gary Breaux: Las astutas estrategias de Satanás (Gén. 3:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201904_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201904/art/jwb_univ_201904_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">20:41</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201904_14_VIDEO" class="jsNoScroll">David Splane: Invitemos a todos a la Conmemoración (Sal. 118:22)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201904_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201904/art/jwb_univ_201904_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:16</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201904_6_VIDEO" class="jsNoScroll">Mark Noumair: Demostremos humildad (1 Ped. 5:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201904_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201904/art/jwb_univ_201904_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:56</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201904_10_VIDEO" class="jsNoScroll">Christopher Mavor: Abrahán fue amigo de Jehová (Is. 41:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201903_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201903/art/jwb_univ_201903_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:48</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201903_12_VIDEO" class="jsNoScroll">Robert Ciranko: Jehová protege a sus leales (Sal. 97:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201903_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201903/art/jwb_univ_201903_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:52</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201903_10_VIDEO" class="jsNoScroll">Robert Luccioni: Seamos humildes y conservemos la paz (Filip. 2:3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201902_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201902/art/jwb_univ_201902_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:27</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201902_12_VIDEO" class="jsNoScroll">Stephen Lett: El orgullo conduce al desastre (Prov. 16:18)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201902_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201902/art/jwb_univ_201902_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:22</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201902_10_VIDEO" class="jsNoScroll">Harold Corkern: Imitemos a Jesús (Juan 2:25)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201901_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201901/art/jwb_univ_201901_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:09</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201901_2_VIDEO" class="jsNoScroll">Mark Noumair: “Este es el camino” (Is. 30:21)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201812_4_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201812/art/jwb_univ_201812_lss_04_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:25</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201812_4_VIDEO" class="jsNoScroll">Samuel Herd: Acerquémonos a Jehová (Sant. 4:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201812_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201812/art/jwb_univ_201812_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:36</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201812_2_VIDEO" class="jsNoScroll">Geoffrey Jackson: Probemos a Jehová de la manera correcta (Mal. 3:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201811_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201811/art/jwb_univ_201811_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:19</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201811_11_VIDEO" class="jsNoScroll">Joel Dellinger: Fortalezcamos nuestra esperanza (Rev. 21:4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201811_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201811/art/jwb_univ_201811_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:44</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201811_7_VIDEO" class="jsNoScroll">Geoffrey Jackson: “Continúen soportándose unos a otros” (Col. 3:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201810_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201810/art/jwb_univ_201810_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">11:40</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201810_12_VIDEO" class="jsNoScroll">Kenneth Flodin: Como siervos de Dios, seamos neutrales (Mat. 10:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201810_4_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201810/univ/art/jwb_univ_201810_lss_04_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:48</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201810_4_VIDEO" class="jsNoScroll">Robert Ciranko: El pueblo de Dios glorifica Su nombre (1 Ped. 2:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201810_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201810/art/jwb_univ_201810_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201810_10_VIDEO" class="jsNoScroll">Gary Breaux: “Manténganse alerta” (Mat. 24:42)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201809_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201809/univ/art/jwb_univ_201809_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:32</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201809_11_VIDEO" class="jsNoScroll">Seth Hyatt: A los insensatos les va mal (Prov. 5:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201809_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201809/art/jwb_univ_201809_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:30</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201809_9_VIDEO" class="jsNoScroll">James Mantz: Evitemos todo tipo de codicia (Luc. 12:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201808_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201808/art/jwb_univ_201808_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:39</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201808_10_VIDEO" class="jsNoScroll">Mark Sanderson: No se confíe (Sant. 4:14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201807_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201807/art/jwb_univ_201807_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:53</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201807_11_VIDEO" class="jsNoScroll">David Splane: "No las conozco" (Mat. 25:12)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201807_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201807/art/jwb_univ_201807_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:17</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201807_10_VIDEO" class="jsNoScroll">John Ekrann: “Háganse imitadores de Dios” (Efes. 5:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201806_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201806/art/jwb_univ_201806_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:37</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201806_3_VIDEO" class="jsNoScroll">William Turner: ¿Podrían distraernos las buenas obras? (Juan 11:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201805_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201805/art/jwb_univ_201805_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:27</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201805_12_VIDEO" class="jsNoScroll">Robert Luccioni: Tres principios útiles para enfrentar la persecución (Juan 15:20)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201804_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201804/univ/art/jwb_univ_201804_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:09</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201804_13_VIDEO" class="jsNoScroll">Kenneth Cook: Cumpla sus promesas y reciba bendiciones (Sal. 15:4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201804_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201804/art/jwb_univ_201804_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:36</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201804_7_VIDEO" class="jsNoScroll">Mark Sanderson: “Pónganse en contra de él” (1 Ped. 5:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201803_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201803/art/jwb_univ_201803_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:01</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201803_11_VIDEO" class="jsNoScroll">Christopher Mavor: Hacer caso de las advertencias nos salvará la vida (Mar. 13:19)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201803_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201803/art/jwb_univ_201803_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:58</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201803_7_VIDEO" class="jsNoScroll">Ronald Curzan: ¿Somos agradables a la vista de Jehová? (Efes. 5:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201803_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201803/art/jwb_univ_201803_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">11:04</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201803_9_VIDEO" class="jsNoScroll">Ralph Walls: Perdonemos a los demás (Rom. 5:12)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201802_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201802/art/jwb_univ_201802_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:50</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201802_12_VIDEO" class="jsNoScroll">David Schafer: Sobrevivamos al gran día (Rev. 16:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201802_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201802/univ/art/jwb_univ_201802_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:20</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201802_8_VIDEO" class="jsNoScroll">Geoffrey Jackson: Seamos fieles como Abrahán (Gén. 12:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201712_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201712/art/jwb_univ_201712_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:07</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201712_3_VIDEO" class="jsNoScroll">Joel Dellinger: No se puede ser esclavo de dos amos (Mat. 6:24)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201711_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201711/art/jwb_univ_201711_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:20</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201711_8_VIDEO" class="jsNoScroll">Gary Breaux: Usemos nuestra capacidad de razonar (2 Tes. 2:1, 2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201711_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201711/art/jwb_univ_201711_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:31</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201711_10_VIDEO" class="jsNoScroll">Joel Dellinger: La cooperación contribuye a la unidad (Luc. 2:41)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201710_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201710/art/jwb_univ_201710_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:21</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201710_11_VIDEO" class="jsNoScroll">William Malenfant: Usemos bien nuestros talentos (Mat. 25:30)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201710_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201710/univ/art/jwb_univ_201710_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:39</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201710_8_VIDEO" class="jsNoScroll">Geoffrey Jackson: Ancianos, ¡vayan al frente! (Luc. 8:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201710_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201710/art/jwb_univ_201710_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:50</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201710_10_VIDEO" class="jsNoScroll">Ronald Curzan: ¡Evite las distracciones, concéntrese! (Luc. 12:14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201709_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201709/art/jwb_univ_201709_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:02</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201709_11_VIDEO" class="jsNoScroll">David Schafer: Miqueas esperó en Jehová (Miq. 7:4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201709_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201709/art/jwb_univ_201709_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:32</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201709_10_VIDEO" class="jsNoScroll">Kenneth Flodin: ¿Seremos humildes o altivos? (Sant. 4:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201709_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201709/art/jwb_univ_201709_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:03</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201709_9_VIDEO" class="jsNoScroll">James Mantz: “Toda cosa a gente de toda clase” (1 Cor. 9:22)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201708_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201708/univ/art/jwb_univ_201708_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:28</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201708_12_VIDEO" class="jsNoScroll">Mark Noumair: Jesús honró a Jehová con su cuerpo (1 Cor. 11:24)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201708_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201708/univ/art/jwb_univ_201708_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:53</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201708_8_VIDEO" class="jsNoScroll">M. Stephen Lett: Esposo, ama a tu esposa como a ti mismo (Cant. de Cant. 8:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201708_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201708/univ/art/jwb_univ_201708_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:30</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201708_10_VIDEO" class="jsNoScroll">William Malenfant: Hagamos sacrificios de buena gana (Sal. 54:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201707_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201707/art/jwb_univ_201707_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:22</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201707_11_VIDEO" class="jsNoScroll">Harold Corkern: Protejamos nuestra amistad con Jehová (Col. 3:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201707_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201707/art/jwb_univ_201707_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:33</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201707_9_VIDEO" class="jsNoScroll">Seth Hyatt: Decida con la ayuda de Jehová (2&nbsp;Crón. 16:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201706_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201706/art/jwb_univ_201706_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:46</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201706_11_VIDEO" class="jsNoScroll">Gary Breaux: No se deje atrapar (Col. 2:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201706_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201706/art/jwb_univ_201706_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:25</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201706_10_VIDEO" class="jsNoScroll">M. Stephen Lett: Escuchemos para entender (Mat. 13:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201706_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201706/art/jwb_univ_201706_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:30</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201706_9_VIDEO" class="jsNoScroll">William Malenfant: La moralidad en estos últimos días (2 Tim. 3:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201705/art/jwb_univ_201705_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:48</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_14_VIDEO" class="jsNoScroll">Kenneth Flodin: “Mejor es el fin de un asunto” (Ecl. 7:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201705/art/jwb_univ_201705_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">11:22</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_13_VIDEO" class="jsNoScroll">David H. Splane: El sitio jw.org, toda una bendición (Isa. 60:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201705/art/jwb_univ_201705_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:09</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_12_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Jesús cumplió la Ley (Mat. 5:43)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_16_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201705/art/jwb_univ_201705_lss_16_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:29</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_16_VIDEO" class="jsNoScroll">Mark Sanderson: Seremos perseguidos (Mat. 10:22)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201705/art/jwb_univ_201705_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:34</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_11_VIDEO" class="jsNoScroll">Mark Noumair: Para ser íntegros, necesitamos orar (Mat. 26:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201704_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201704/art/jwb_univ_201704_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:10</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201704_11_VIDEO" class="jsNoScroll">Mark Noumair: El estudio profundo nos acerca a Jehová (Sal. 73:28)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201704_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201704/art/jwb_univ_201704_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:12</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201704_7_VIDEO" class="jsNoScroll">Izak Marais: Busquemos primero el Reino (Mat. 6:33)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201703_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201703/univ/art/jwb_univ_201703_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:50</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201703_13_VIDEO" class="jsNoScroll">David Schafer: Jehová guía a su pueblo (Sal. 73:24)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201703_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201703/art/jwb_univ_201703_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:10</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201703_12_VIDEO" class="jsNoScroll">David H. Splane: Seamos flexibles por causa de las buenas nuevas (1&nbsp;Cor. 9:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201703_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201703/univ/art/jwb_univ_201703_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:23</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201703_11_VIDEO" class="jsNoScroll">Mark Sanderson: Jehová cuida a los enfermos (Hech. 15:29)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201702_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201702/art/jwb_univ_201702_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:17</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201702_10_VIDEO" class="jsNoScroll">Harold Corkern: Oremos para conseguir “la paz de Dios” (Filip. 4:7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201702_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201702/univ/art/jwb_univ_201702_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:09</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201702_6_VIDEO" class="jsNoScroll">Geoffrey Jackson: ¿Por qué es tan importante ser neutrales? (Miq. 4:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201701_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201701/art/jwb_univ_201701_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:58</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201701_12_VIDEO" class="jsNoScroll">Joel Dellinger: Mantengamos una actitud de espera (Mat. 18:14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201701_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201701/art/jwb_univ_201701_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:33</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201701_11_VIDEO" class="jsNoScroll">Izak Marais: Todos somos necesarios (1 Cor. 12:22)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201701_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201701/art/jwb_univ_201701_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:43</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201701_9_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Un mensaje que llega “hasta la parte más distante de la tierra” (Hech. 1:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201612_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201612/art/jwbmw_univ_201612_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:38</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201612_1_VIDEO" class="jsNoScroll">Robert Luccioni: Que nada limite lo que usted puede dar (Amós 7:14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201612_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201612/art/jwbmw_univ_201612_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:22</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201612_2_VIDEO" class="jsNoScroll">M. Stephen Lett: Mostremos favor al de condición humilde (Prov.&nbsp;19:17)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201611_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201611/art/jwbmw_univ_201611_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:54</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201611_1_VIDEO" class="jsNoScroll">John Ekrann: El rescate sí es para usted (Gál. 2:20)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201610_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201610/art/jwbmw_univ_201610_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:30</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201610_2_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: “Una palabra a su tiempo apropiado” (Prov. 15:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201610_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201610/art/jwbmw_univ_201610_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:00</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201610_1_VIDEO" class="jsNoScroll">M. Stephen Lett: Nunca hagamos tropezar a otros (2 Cor. 6:3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201609_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201609/art/jwbmw_univ_201609_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:13</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201609_1_VIDEO" class="jsNoScroll">M. Stephen Lett: Gane la batalla en su interior (Rom. 7:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201608_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbmw/201608/univ/art/jwbmw_univ_201608_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:09</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201608_2_VIDEO" class="jsNoScroll">Samuel F.&nbsp;Herd: Servir a Jehová como esclavos es todo un honor (Mat. 24:45)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201608_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201608/art/jwbmw_univ_201608_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:18</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201608_1_VIDEO" class="jsNoScroll">David H. Splane: Las decisiones del “esclavo fiel y discreto” (Mat. 24:45)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201607_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbmw/201607/univ/art/jwbmw_univ_201607_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:32</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201607_2_VIDEO" class="jsNoScroll">Kenneth Flodin: Cuidémonos de los engaños (Jud. 9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201607_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201607/art/jwbmw_univ_201607_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:01</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201607_1_VIDEO" class="jsNoScroll">Mark Sanderson: ¿Podemos acelerar la llegada del día de Jehová? (2 Ped. 3:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201606_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201606/art/jwbmw_univ_201606_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:41</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201606_1_VIDEO" class="jsNoScroll">Gerrit Lösch: No guardemos rencor (1&nbsp;Cor. 13:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201605_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201605/art/jwbmw_univ_201605_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:05</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201605_2_VIDEO" class="jsNoScroll">Samuel F. Herd: Jehová nunca olvidará el amor de ustedes (Sal. 71:18)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201605_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201605/art/jwbmw_univ_201605_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201605_1_VIDEO" class="jsNoScroll">David Schafer: Practiquemos la devoción piadosa en nuestra propia casa (1&nbsp;Tim. 5:4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201604_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201604/art/jwbmw_univ_201604_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:14</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201604_2_VIDEO" class="jsNoScroll">Mark Sanderson: Enfrentemos los cambios con fe y confianza (Heb. 13:17)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201603_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201603/art/jwbmw_univ_201603_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:41</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201603_3_VIDEO" class="jsNoScroll">Gary Breaux: Una guerra en nuestro interior (1 Ped.&nbsp;2:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201603_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201603/art/jwbmw_univ_201603_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:27</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201603_2_VIDEO" class="jsNoScroll">Robert Ciranko: Nuestros queridos hermanos de edad avanzada (Lev.&nbsp;19:32)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201603_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201603/art/jwbmw_univ_201603_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:26</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201603_1_VIDEO" class="jsNoScroll">Kenneth Flodin: “Un escondite contra el viento” (Is. 32:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201602_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201602/art/jwbmw_univ_201602_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:16</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201602_3_VIDEO" class="jsNoScroll">Christopher Mavor: Los jóvenes valen mucho a los ojos de Jehová (Sal. 148:12, 13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201602_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201602/art/jwbmw_univ_201602_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:01</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201602_2_VIDEO" class="jsNoScroll">David Schafer: Cuidado con el exceso de confianza (Mat. 26:33)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201602_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbmw/201602/univ/art/jwbmw_univ_201602_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:09</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201602_1_VIDEO" class="jsNoScroll">Robert Luccioni: Desarrollemos la lengua de los sabios (Prov. 12:18)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201601_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201601/art/jwbmw_univ_201601_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:50</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201601_1_VIDEO" class="jsNoScroll">Patrick LaFranca: Jehová desea que seamos generosos (Prov. 3:27)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201512_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201512/art/jwbmw_univ_201512_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201512_3_VIDEO" class="jsNoScroll">William Malenfant: “Porque eres justo” (Neh. 9:7, 8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201512_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbmw/201512/univ/art/jwbmw_univ_201512_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:17</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201512_1_VIDEO" class="jsNoScroll">David Splane: "Isaac se enamoró de ella" (Gén. 24:67)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201512_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201512/art/jwbmw_univ_201512_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:43</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201512_2_VIDEO" class="jsNoScroll">Izak Marais: “Cuando vean todas estas cosas” (Mat. 24:33)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201511_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201511/art/jwbmw_univ_201511_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:00</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201511_2_VIDEO" class="jsNoScroll">James Mantz: “Tú creaste todas las cosas” (Rev. 4:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201511_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201511/art/jwbmw_univ_201511_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201511_3_VIDEO" class="jsNoScroll">Kenneth Flodin: “De ningún modo pasará esta generación” (Mat. 24:34)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201511_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201511/art/jwbmw_univ_201511_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:26</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201511_1_VIDEO" class="jsNoScroll">Ronald Curzan: “Llegue a ti mi propio clamor por ayuda” (Sal. 102:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201510_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201510/art/jwbmw_univ_201510_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:11</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201510_2_VIDEO" class="jsNoScroll">Alex Reinmueller: ¿Cómo podemos ser justos? (Hech. 10:34)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201510_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201510/art/jwbmw_univ_201510_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:19</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201510_1_VIDEO" class="jsNoScroll">Joel Dellinger: El “arma secreta” de Ezequías (2 Crón. 29:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201508_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201508/art/jwbmw_univ_201508_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:58</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201508_2_VIDEO" class="jsNoScroll">M. Stephen Lett: “Me deleito en la ley de Dios” (Rom. 7:22)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201508_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201508/art/jwbmw_univ_201508_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:41</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201508_1_VIDEO" class="jsNoScroll">Robert Luccioni: No amemos al mundo (1 Juan 2:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201507_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201507/art/jwbmw_univ_201507_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:11</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201507_2_VIDEO" class="jsNoScroll">David Schafer: “Su deleite está en la ley” (Sal. 1:2, 3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201507_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201507/art/jwbmw_univ_201507_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:34</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201507_1_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Consideremos a los demás superiores a nosotros (Filip. 2:3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201506_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201506/art/jwbmw_univ_201506_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:28</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201506_2_VIDEO" class="jsNoScroll">William Malenfant: No nos dejemos engañar por los malvados (2 Tes. 2:1, 2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201506_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201506/art/jwbmw_univ_201506_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:00</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201506_1_VIDEO" class="jsNoScroll">David H. Splane: El “esclavo” no tiene 1.900 años de existencia (Mat. 24:45)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201505_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201505/art/jwbmw_univ_201505_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">6:59</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201505_1_VIDEO" class="jsNoScroll">Mark Sanderson: Estemos dispuestos a abrir nuestra mano (Prov. 3:27)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-es ml-S ms-ROMAN" lang="es" xml:lang="es" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201503_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201503/art/jwbmw_univ_201503_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:49</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/es/biblioteca/videos/#es/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201503_2_VIDEO" class="jsNoScroll">Robert Ciranko: ¿Valoramos nuestras reuniones? (Sal. 27:11)</a>
         </h3>
         
      </div>
   </div>




         

         </div>
    """

    english_html = """
    <div class="synopsisGroup">

         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_19_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_19_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:08</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_19_VIDEO" class="jsNoScroll">Gary Breaux: Protect Yourself From Misinformation (Dan. 11:27)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_18_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_18_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:03</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_18_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Be Transformed, Not Disguised (Rom. 12:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-111_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-111/univ/art/jwb-111_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">11:08</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-111_6_VIDEO" class="jsNoScroll">Harold Corkern: Satan Cannot Fool Righteous Ones (2 Cor. 2:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_17_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_17_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:53</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_17_VIDEO" class="jsNoScroll">Troy Snyder: Help for the Discouraged (Ps. 34:18)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_16_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_16_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:25</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_16_VIDEO" class="jsNoScroll">Clive Martin: Render Sacred Service With Godly Fear (Ps. 86:11, 12)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_15_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_15_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:23</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_15_VIDEO" class="jsNoScroll">Leonard Myers: Jehovah Rewards His Faithful Servants (Heb. 11:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:39</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_14_VIDEO" class="jsNoScroll">Mark Noumair: Jehovah Is With Them (Zech. 8:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-110_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-110/univ/art/jwb-110_univ_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:45</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-110_7_VIDEO" class="jsNoScroll">Mark Sanderson: ‘Peace of God Surpasses Understanding’ (Phil. 4:6, 7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">29:04</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_1_VIDEO" class="jsNoScroll">2024 Memorial Morning Worship—Kenneth Cook, Jr.: How Should We Remember Jesus? (Luke 22:19)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:52</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_12_VIDEO" class="jsNoScroll">Robert Luccioni: “Do You Believe This?” (John 11:26)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:07</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_13_VIDEO" class="jsNoScroll">James Mantz: Avoid the Snare of Greed (Col. 3:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:54</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_10_VIDEO" class="jsNoScroll">Gage Fleegle: Benefiting From Prohibitions (Eccl. 7:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_9_VIDEO" class="jsNoScroll">Jonathan Smith: See the Bigger Picture (1 Sam. 17:42)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-099_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-099/univ/art/jwb-099_univ_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-099_7_VIDEO" class="jsNoScroll">Seth Hyatt: Speaking Truth Though Labeled as Deceivers (2 Cor. 6:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:13</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_8_VIDEO" class="jsNoScroll">Kenneth Godburn: Listen With Mildness (Jas. 1:19-21)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:04</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_7_VIDEO" class="jsNoScroll">Donald Gordon: “Pay Constant Attention to .  .  . Your Teaching” (1 Tim. 4:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:14</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_6_VIDEO" class="jsNoScroll">Nicholas Ahladis: Jehovah Cares for the “Little Ones” (Matt. 18:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_5_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_05_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:58</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_5_VIDEO" class="jsNoScroll">Robert Ciranko: How to Be a True Friend (Matt. 7:12)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_4_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_04_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:50</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_4_VIDEO" class="jsNoScroll">Kenneth Flodin: Learn From Errors (Phil. 3:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbvod24/univ/art/jwbvod24_univ_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:46</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbvod24_3_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Honor the Superior Authorities (Rom. 13:7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-107_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-107/univ/art/jwb-107_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:06</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-107_12_VIDEO" class="jsNoScroll">John Ekrann: How Can We Successfully Overcome Misunderstandings? (Acts 15:37-39)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-107_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-107/univ/art/jwb-107_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:03</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-107_11_VIDEO" class="jsNoScroll">M. Stephen Lett: Help Young Ones Progress (Mark 10:13, 14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-108_16_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-108/univ/art/jwb-108_univ_lss_16_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:07</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-108_16_VIDEO" class="jsNoScroll">Leonard Myers: The Transfiguration Builds Faith (2 Pet. 1:19)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-108_15_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-108/univ/art/jwb-108_univ_lss_15_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:12</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-108_15_VIDEO" class="jsNoScroll">Anthony Griffin: The Refreshing Way Jehovah Deals With Us (Deut. 32:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-108_17_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-108/univ/art/jwb-108_univ_lss_17_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-108_17_VIDEO" class="jsNoScroll">William Malenfant: Elihu Patiently Listened (Jas. 1:19)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-108_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-108/univ/art/jwb-108_univ_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:59</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-108_14_VIDEO" class="jsNoScroll">Jeffrey Winder: Our Modesty Benefits Others (Matt. 22:39)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-106_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-106/univ/art/jwb-106_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:03</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-106_11_VIDEO" class="jsNoScroll">Clive Martin: Imitate the Humility of the Great Shepherd (Ps. 18:35)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-106_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-106/univ/art/jwb-106_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:48</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-106_10_VIDEO" class="jsNoScroll">Paul Gillies: Reflect Jehovah’s Personality by Imitating Jesus (Eph. 4:20, 21)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-106_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-106/univ/art/jwb-106_univ_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:18</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-106_3_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Creating Opportunities to Give a Witness (John 4:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-106_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-106/univ/art/jwb-106_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:12</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-106_9_VIDEO" class="jsNoScroll">Joel Dellinger: Understanding Prophecy Motivates Us (Rev. 7:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-105_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-105/univ/art/jwb-105_univ_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:42</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-105_8_VIDEO" class="jsNoScroll">Harold Corkern: Imitate God by Valuing Others and Their Work (Heb. 6:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-102/univ/art/jwb-102_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:31</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_11_VIDEO" class="jsNoScroll">Gage Fleegle: Jehovah’s Precious Gift, the Holy Spirit (John 3:34)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-102/univ/art/jwb-102_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:01</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_10_VIDEO" class="jsNoScroll">David Schafer: ‘Trust in Jehovah and Do Good’ (Ps. 37:3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-102/univ/art/jwb-102_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:05</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_6_VIDEO" class="jsNoScroll">William Turner, Jr.: What Makes Us Valuable to Jehovah? (1 Pet. 3:4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-102/univ/art/jwb-102_univ_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:29</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_8_VIDEO" class="jsNoScroll">Gajus Glockentin: Reject Improper Instant Gratification (Titus 2:12)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-102/univ/art/jwb-102_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:25</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-102_9_VIDEO" class="jsNoScroll">Robert Luccioni: Accomplishing Assignments Jehovah’s Way (John 5:19)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-101/univ/art/jwb-101_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:55</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_12_VIDEO" class="jsNoScroll">Hermanus van Selm: Jehovah Cares for the Humble (Isa. 57:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-101/univ/art/jwb-101_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:16</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_11_VIDEO" class="jsNoScroll">John Ekrann: “Lovers of Money” (2 Tim. 3:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_5_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-101/univ/art/jwb-101_univ_lss_05_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:05</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_5_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Qualities of a Good Teacher (1 Thess. 2:7, 8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-101/univ/art/jwb-101_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:35</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_9_VIDEO" class="jsNoScroll">Mark Noumair: Jehovah Encourages His Servant (Jer. 15:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-101/univ/art/jwb-101_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:17</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-101_10_VIDEO" class="jsNoScroll">Seth Hyatt: Uphold Jehovah’s View of Marriage (Mark 10:11, 12)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-105_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-105/univ/art/jwb-105_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:52</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-105_9_VIDEO" class="jsNoScroll">Christopher Mavor: We Must Examine Our Motives (Prov. 16:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-099_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-099/univ/art/jwb-099_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:33</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-099_12_VIDEO" class="jsNoScroll">Ronald Curzan: “Dwell Together in Unity!” (Ps. 133:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-105_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-105/univ/art/jwb-105_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:43</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-105_12_VIDEO" class="jsNoScroll">David H. Splane: ‘Readjust Others in a Spirit of Mildness’ (Gal. 6:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-099_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-099/univ/art/jwb-099_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:44</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-099_11_VIDEO" class="jsNoScroll">Robert Ciranko: Discipline Is From Jehovah (1 Cor. 5:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-099_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-099/univ/art/jwb-099_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:38</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-099_10_VIDEO" class="jsNoScroll">Gary Breaux: Prepare Your Heart for Prayer (Ezra 7:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-104_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-104/univ/art/jwb-104_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:44</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-104_11_VIDEO" class="jsNoScroll">Leonard Myers: Show Love to Unbelieving Relatives While Being Loyal to Jehovah (Matt. 10:34, 35)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-104_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-104/univ/art/jwb-104_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-104_10_VIDEO" class="jsNoScroll">Alex Reinmueller: Keep Up the Fight Against Sin! (Rom. 7:22, 23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-096/univ/art/jwb-096_univ_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:50</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_14_VIDEO" class="jsNoScroll">Baltasar Perla, Jr.: Acquire and Maintain Humility (1 Pet. 5:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-096/univ/art/jwb-096_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:17</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_13_VIDEO" class="jsNoScroll">David H. Splane: “All Scripture Is Inspired” (2 Tim. 3:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-096/univ/art/jwb-096_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:06</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_6_VIDEO" class="jsNoScroll">M. Stephen Lett: Never Let Satan Intimidate You (Deut. 1:17)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-096/univ/art/jwb-096_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:48</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_12_VIDEO" class="jsNoScroll">Joel Dellinger: “Always Rejoice in the Lord” (Phil. 4:4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-096/univ/art/jwb-096_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:49</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-096_11_VIDEO" class="jsNoScroll">William Malenfant: Comparing the Spiritual and Physical Person (1 Cor. 2:12-15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-095_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-095/univ/art/jwb-095_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:55</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-095_12_VIDEO" class="jsNoScroll">Seth Hyatt: Give Gifts of Mercy (Luke 10:37)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-095_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-095/univ/art/jwb-095_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:49</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-095_11_VIDEO" class="jsNoScroll">Patrick LaFranca: Continue to Acquire Wisdom Each Day (Prov. 3:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-095_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-095/univ/art/jwb-095_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:51</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-095_6_VIDEO" class="jsNoScroll">Robert Luccioni: Be a Gideon (Eph. 4:1, 2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-095_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-095/univ/art/jwb-095_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:52</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-095_10_VIDEO" class="jsNoScroll">Kenneth Flodin: ‘Jesus’ Yoke Is Kindly’ (Matt. 11:29, 30)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-092/univ/art/jwb-092_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">26:46</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_10_VIDEO" class="jsNoScroll">Memorial Morning Worship—Samuel F. Herd: Annually, “Keep Doing This in Remembrance of Me” (Luke 22:19)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-092/univ/art/jwb-092_univ_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:08</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_14_VIDEO" class="jsNoScroll">Kenneth Cook, Jr.: Avoid Deception, and Follow the Kingdom (Jer. 10:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-092/univ/art/jwb-092_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:18</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_13_VIDEO" class="jsNoScroll">Izak Marais: Always Be Gracious in Your Speech (Col. 4:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-092/univ/art/jwb-092_univ_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:32</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_7_VIDEO" class="jsNoScroll">David Schafer: Share a Word of Encouragement (Acts 13:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-092/univ/art/jwb-092_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:43</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_11_VIDEO" class="jsNoScroll">John Ekrann: Build Faith in the Resurrection (Acts 9:40)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-092/univ/art/jwb-092_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-092_12_VIDEO" class="jsNoScroll">Gajus Glockentin: The Ransom Protects Our Precious Unity (John 10:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-103_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-103/univ/art/jwb-103_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:26</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-103_13_VIDEO" class="jsNoScroll">James Mantz: “Make Friends . . . by Means of Unrighteous Riches” (Luke 16:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-103_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-103/univ/art/jwb-103_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:55</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-103_12_VIDEO" class="jsNoScroll">M. Stephen Lett: Beware of the Power of Materialism (Matt. 6:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-103_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-103/univ/art/jwb-103_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:02</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-103_11_VIDEO" class="jsNoScroll">Mark Noumair: “It Will Not Be Late!” (Hab. 2:3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-103_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-103/univ/art/jwb-103_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">11:00</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-103_10_VIDEO" class="jsNoScroll">Ronald Curzan: Be “a True Friend” (Prov. 17:17)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-100_19_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-100/univ/art/jwb-100_univ_lss_19_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-100_19_VIDEO" class="jsNoScroll">Christopher Mavor: Draw Close to God Through Prayer (Eph. 6:18)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-100_18_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-100/univ/art/jwb-100_univ_lss_18_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:52</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-100_18_VIDEO" class="jsNoScroll">Hermanus van Selm: The Connection Between Compassion and the Ransom (1 John 4:9-11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-100_20_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-100/univ/art/jwb-100_univ_lss_20_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:00</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-100_20_VIDEO" class="jsNoScroll">Clive Martin: Imitate Sarah’s Faith in Jehovah! (Heb. 11:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-100_17_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-100/univ/art/jwb-100_univ_lss_17_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:25</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-100_17_VIDEO" class="jsNoScroll">Gary Breaux: The Older Men and the Superior Authorities Standing in Their Proper Place (Rom. 13:1-4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-098_15_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-098/univ/art/jwb-098_univ_lss_15_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:18</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-098_15_VIDEO" class="jsNoScroll">Seth Hyatt: “Bear Fruit With Endurance” Despite Trials (Luke 8:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-098_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-098/univ/art/jwb-098_univ_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:20</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-098_14_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: “The Meek Will Possess the Earth” (Ps. 37:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-094_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-094/univ/art/jwb-094_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:59</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-094_13_VIDEO" class="jsNoScroll">Robert Luccioni: Guard Yourself Respecting a Treacherous Spirit (Mal. 2:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-094_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-094/univ/art/jwb-094_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:13</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-094_12_VIDEO" class="jsNoScroll">Kenneth Flodin: ‘Do Good and Share’ (Heb. 13:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-094_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-094/univ/art/jwb-094_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:00</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-094_6_VIDEO" class="jsNoScroll">David H. Splane: “Safeguard Your Heart” (Prov. 4:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-094_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-094/univ/art/jwb-094_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:12</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-094_11_VIDEO" class="jsNoScroll">Joel Dellinger: Jehovah’s Day “Will Not Be Late!” (Hab. 2:3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-093/univ/art/jwb-093_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:52</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_13_VIDEO" class="jsNoScroll">Mark Sanderson: They Proved Themselves Faultless (1 Ki. 15:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-093/univ/art/jwb-093_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:46</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_12_VIDEO" class="jsNoScroll">Ronald Curzan: Show Appreciation for All of Jehovah’s Provisions  (Ps. 116:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-093/univ/art/jwb-093_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:03</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_11_VIDEO" class="jsNoScroll">John Ekrann: Stick to Jehovah’s Requirements, and Obey Theocratic Direction (Acts 15:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-093/univ/art/jwb-093_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:17</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_10_VIDEO" class="jsNoScroll">Samuel F. Herd: “I Was Given a Thorn in the Flesh” (2 Cor. 12:7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-093/univ/art/jwb-093_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:10</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-093_6_VIDEO" class="jsNoScroll">William Turner, Jr.: Do Not Be Partial (John 4:31)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-090_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-090/univ/art/jwb-090_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:21</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-090_13_VIDEO" class="jsNoScroll">Gajus Glockentin: ‘Make Friends by Means of Unrighteous Riches’ (Luke 16:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-090_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-090/univ/art/jwb-090_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:46</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-090_10_VIDEO" class="jsNoScroll">David Schafer: We Live in the Time of the Harvest (Matt. 9:37)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-090_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-090/univ/art/jwb-090_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:47</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-090_12_VIDEO" class="jsNoScroll">Izak Marais: Benefit From Jehovah’s Loving Discipline (Heb. 12:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-090_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-090/univ/art/jwb-090_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:41</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-090_11_VIDEO" class="jsNoScroll">Kenneth Cook, Jr.: “Hold Fast to What You Have Until I Come” (Rev. 2:25)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-091_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-091/univ/art/jwb-091_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:41</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-091_6_VIDEO" class="jsNoScroll">Christopher Mavor: Jehovah Loves His People (Isa. 54:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-091_5_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-091/univ/art/jwb-091_univ_lss_05_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:13</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-091_5_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Keep “the Belt of Truth” Tight (Eph. 6:14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-089_15_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-089/univ/art/jwb-089_univ_lss_15_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:40</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-089_15_VIDEO" class="jsNoScroll">Leon Weaver, Jr.: Don’t Give Up in Preaching—Circumstances Change (Acts 16:26-31)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-089_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-089/univ/art/jwb-089_univ_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-089_14_VIDEO" class="jsNoScroll">Kenneth Flodin: The Quality of Meekness (Num. 12:3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-089_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-089/univ/art/jwb-089_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:48</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-089_12_VIDEO" class="jsNoScroll">Gary Breaux: Storytelling Is an Effective Teaching Tool (1 John 5:19)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-089_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-089/univ/art/jwb-089_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:39</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-089_13_VIDEO" class="jsNoScroll">Clive Martin: What Does Jehovah Look For in Us? (Prov. 27:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-088/univ/art/jwb-088_univ_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:31</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_14_VIDEO" class="jsNoScroll">Seth Hyatt: Choose “the Good Portion” (Luke 10:42)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-088/univ/art/jwb-088_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:43</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_13_VIDEO" class="jsNoScroll">Joel Dellinger: Your Deliverance Is Getting Near (Rev. 6:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-088/univ/art/jwb-088_univ_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_7_VIDEO" class="jsNoScroll">William Malenfant: Spiritually Mature Youths (Prov. 20:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-088/univ/art/jwb-088_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:34</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_12_VIDEO" class="jsNoScroll">Hermanus van Selm: Our Heart and Jehovah’s Thinking (Ps. 119:97)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-088/univ/art/jwb-088_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:58</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_10_VIDEO" class="jsNoScroll">Mark Noumair: Prepare for Persecution (1 Pet. 4:4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-088/univ/art/jwb-088_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">16:55</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-088_9_VIDEO" class="jsNoScroll">Memorial Morning Worship—Gerrit Lösch: Jehovah Restores His Original Purpose (Gen. 2:15-17)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-087_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-087/univ/art/jwb-087_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:08</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-087_12_VIDEO" class="jsNoScroll">Patrick LaFranca: ‘Remember Your Grand Creator’ (Eccl. 12:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-087_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-087/univ/art/jwb-087_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:34</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-087_11_VIDEO" class="jsNoScroll">Robert Luccioni: “Do Not Forget Hospitality” (Heb. 13:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-087_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-087/univ/art/jwb-087_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">11:04</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-087_10_VIDEO" class="jsNoScroll">Harold Corkern: “Buy Truth and Never Sell It” (Prov. 23:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-097_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-097/univ/art/jwb-097_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:00</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-097_13_VIDEO" class="jsNoScroll">John Ekrann: Become Gentle to One Another (1 Thess. 2:7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-097_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-097/univ/art/jwb-097_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:12</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-097_12_VIDEO" class="jsNoScroll">Kenneth Cook, Jr: Everlasting Life Is Worth Any Sacrifice (Mark 10:29, 30)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-097_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-097/univ/art/jwb-097_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:43</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-097_11_VIDEO" class="jsNoScroll">David Schafer: “Be Absorbed in Them” (1 Tim. 4:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-097_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-097/univ/art/jwb-097_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:23</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-097_10_VIDEO" class="jsNoScroll">James Mantz: Jehovah Provides True Freedom (2 Cor. 3:17)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-086_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-086/univ/art/jwb-086_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:26</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-086_10_VIDEO" class="jsNoScroll">Izak Marais: Patiently Wait on Jehovah (Hab. 2:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-086_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-086/univ/art/jwb-086_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-086_9_VIDEO" class="jsNoScroll">Leonard Myers: Remain Watchful for “Peace and Security!” (1 Thess. 5:3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-086_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-086/univ/art/jwb-086_univ_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:19</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-086_2_VIDEO" class="jsNoScroll">William Malenfant: Satan Is “the Father of the Lie” (John 8:44)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-086_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-086/univ/art/jwb-086_univ_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:42</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-086_8_VIDEO" class="jsNoScroll">Ronald Curzan: Marriage Mates “Become One Flesh” (Gen. 2:24)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-085_16_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-085/univ/art/jwb-085_univ_lss_16_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:59</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-085_16_VIDEO" class="jsNoScroll">Robert Luccioni: “Pressing on Toward the Goal” (Phil. 3:14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-085_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-085/univ/art/jwb-085_univ_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:37</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-085_2_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Assisting Our Brothers Materially (Prov. 19:17)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-084_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-084/univ/art/jwb-084_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-084_10_VIDEO" class="jsNoScroll">Mark Noumair: Keep Spinning on the Potter’s Wheel (Josh. 1:1, 2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-084_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-084/univ/art/jwb-084_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:43</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-084_9_VIDEO" class="jsNoScroll">M. Stephen Lett: Tap Into "the Power Beyond What Is Normal" (2 Cor. 4:7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-084_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-084/univ/art/jwb-084_univ_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:21</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-084_7_VIDEO" class="jsNoScroll">Gajus Glockentin: How to Be Resilient (Luke 10:39)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-083_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-083/univ/art/jwb-083_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:58</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-083_10_VIDEO" class="jsNoScroll">Hermanus van Selm: Obedience Is a Protection (2 Thess. 1:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-083_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-083/univ/art/jwb-083_univ_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:30</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-083_11_VIDEO" class="jsNoScroll">Mark Sanderson: “I Give You My Peace” (John 14:27)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-083_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-083/univ/art/jwb-083_univ_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-083_6_VIDEO" class="jsNoScroll">William Turner, Jr.: Comfort and Strengthen One Another (2 Thess. 2:16, 17)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-082_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-082/univ/art/jwb-082_univ_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-082_10_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Faithful With Material Things (Luke 16:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-082_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-082/univ/art/jwb-082_univ_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:20</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-082_9_VIDEO" class="jsNoScroll">Kenneth Flodin: “The Plans of the Diligent” (Prov. 21:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-081_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-081/univ/art/jwb-081_univ_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:51</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-081_2_VIDEO" class="jsNoScroll">M. Stephen Lett: See the Big Picture (Acts 8:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-080_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-080/univ/art/jwb-080_univ_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:25</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-080_13_VIDEO" class="jsNoScroll">Hermanus van Selm: “Take Courage!” (John 16:33)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-080_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb-080/univ/art/jwb-080_univ_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:40</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-080_7_VIDEO" class="jsNoScroll">David H. Splane: We Serve the God of True Prophecy (Ps. 46:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-080_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb-080/univ/art/jwb-080_univ_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:55</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb-080_12_VIDEO" class="jsNoScroll">Gajus Glockentin: Why Reach Out? (1 Tim. 3:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202104_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202104/univ/art/jwb_univ_202104_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:10</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202104_7_VIDEO" class="jsNoScroll">Gary Breaux: Let Jehovah Mold You (Isa. 64:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202104_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202104/art/jwb_univ_202104_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:43</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202104_9_VIDEO" class="jsNoScroll">William Turner, Jr.: “Jehovah Raises Up the Meek” (Ps. 147:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202103_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202103/art/jwb_univ_202103_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:21</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202103_12_VIDEO" class="jsNoScroll">Izak Marais: "Deaden . . . Your Body Members" (Col. 3:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202103_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202103/art/jwb_univ_202103_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">26:10</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202103_13_VIDEO" class="jsNoScroll">Memorial Morning Worship—M. Stephen Lett: “The Spirit Itself Bears Witness With Our Spirit” (Rom. 8:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202103_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202103/univ/art/jwb_univ_202103_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:21</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202103_8_VIDEO" class="jsNoScroll">Robert Ciranko: “They Will Become One Flesh” (Gen. 2:24)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202103_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202103/art/jwb_univ_202103_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202103_9_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Continue to "Be Transformed" (Rom. 12:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202102_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202102/art/jwb_univ_202102_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">12:00</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202102_12_VIDEO" class="jsNoScroll">Mark Sanderson: Keep the Mental Attitude of Christ (Phil. 2:5, 7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202102_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202102/art/jwb_univ_202102_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:23</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202102_11_VIDEO" class="jsNoScroll">Mark Noumair: “Ezra Had Prepared His Heart” (Ezra 7:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202102_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202102/art/jwb_univ_202102_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:21</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202102_10_VIDEO" class="jsNoScroll">Alex Reinmueller: "Jehovah Our God Is One Jehovah" (Deut. 6:4, 5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202101_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202101/art/jwb_univ_202101_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:01</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202101_13_VIDEO" class="jsNoScroll">James Mantz: “Do Not Be Quick to Take Offense” (Eccl. 7:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202101_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202101/univ/art/jwb_univ_202101_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:15</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202101_12_VIDEO" class="jsNoScroll">Joel Dellinger: Faith—"Assured Expectation" (Heb. 11:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202012_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202012/art/jwb_univ_202012_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:36</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202012_11_VIDEO" class="jsNoScroll">Leonard Myers: “Have . . . Concern for One Another” (1 Cor. 12:25)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202012_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202012/art/jwb_univ_202012_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:04</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202012_6_VIDEO" class="jsNoScroll">William Malenfant: Learning a New Language (Neh. 13:24)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202012_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202012/art/jwb_univ_202012_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202012_9_VIDEO" class="jsNoScroll">Mark Noumair: Our Witnessing Conquers Satan (Rev. 12:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202011_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202011/art/jwb_univ_202011_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:09</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202011_11_VIDEO" class="jsNoScroll">Robert Luccioni: Strengthen Your Spiritual Core (2 Tim. 3:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202011_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202011/art/jwb_univ_202011_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:36</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202011_7_VIDEO" class="jsNoScroll">Joel Dellinger: Be a Discerning Student (Prov. 3:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202011_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202011/art/jwb_univ_202011_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:53</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202011_9_VIDEO" class="jsNoScroll">Ronald Curzan: Our Hope of the Resurrection (Acts 24:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202010_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202010/art/jwb_univ_202010_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:50</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202010_12_VIDEO" class="jsNoScroll">Gene Smalley: Do I Forgive Others? (Luke 18:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202010_16_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202010/art/jwb_univ_202010_lss_16_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:11</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202010_16_VIDEO" class="jsNoScroll">Robert Luccioni: Another Convenient Time (Luke 4:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202010_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202010/art/jwb_univ_202010_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:52</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202010_6_VIDEO" class="jsNoScroll">Harold Corkern: Stand Firm Against Our Enemy (1 Pet. 5:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202010_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202010/art/jwb_univ_202010_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:41</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202010_9_VIDEO" class="jsNoScroll">M. Stephen Lett: “Draw Close to God” (Jas. 4:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202009_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202009/art/jwb_univ_202009_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:26</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202009_8_VIDEO" class="jsNoScroll">William Turner, Jr.: Make Known “the Good News” (Rom. 1:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202009_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202009/art/jwb_univ_202009_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:33</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202009_10_VIDEO" class="jsNoScroll">Mark Sanderson: “Wisdom Is With the Modest Ones” (Prov. 11:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202007_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202007/art/jwb_univ_202007_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:35</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202007_11_VIDEO" class="jsNoScroll">Ralph Walls: “Ponder Over These Things” (1 Tim. 4:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202007_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202007/art/jwb_univ_202007_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:37</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202007_10_VIDEO" class="jsNoScroll">Gajus Glockentin: Protect Yourself From Lies (Col. 3:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202006_5_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202006/art/jwb_univ_202006_lss_05_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:38</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202006_5_VIDEO" class="jsNoScroll">Leonard Myers: Be Reasonable in the Family (Col. 3:18-20)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202006_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202006/art/jwb_univ_202006_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:17</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202006_2_VIDEO" class="jsNoScroll">Alex Reinmueller: If Misjudged, Remain Loyal (1 Sam. 20:30)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202005_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202005/art/jwb_univ_202005_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:06</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202005_11_VIDEO" class="jsNoScroll">David Schafer: Learn to Be Content (Heb. 13:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202005_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202005/art/jwb_univ_202005_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:35</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202005_14_VIDEO" class="jsNoScroll">Mark Sanderson: Seek the Advantage of the Other Person (1 Cor. 10:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202005_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202005/art/jwb_univ_202005_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:42</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202005_9_VIDEO" class="jsNoScroll">William Malenfant: “Become One Flock” (John 10:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202004/univ/art/jwb_univ_202004_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:58</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_14_VIDEO" class="jsNoScroll">Joel Dellinger: Moving Forward With Faith, Not Fear (Isa. 41:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202004/univ/art/jwb_univ_202004_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:07</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_12_VIDEO" class="jsNoScroll">Robert Ciranko: Avoid Flirting and Ego (1 Tim. 5:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202004/art/jwb_univ_202004_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_7_VIDEO" class="jsNoScroll">John Ekrann: Do You See Jehovah’s Hand? (Isa. 66:14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202004/univ/art/jwb_univ_202004_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:12</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_10_VIDEO" class="jsNoScroll">Harold Corkern: Jehovah—“The God of All Comfort” (2 Cor. 1:3, 4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202004/univ/art/jwb_univ_202004_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:14</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_13_VIDEO" class="jsNoScroll">Robert Luccioni: Think God's Thoughts, Not Those of Men (Matt. 16:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202004/art/jwb_univ_202004_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">24:38</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202004_9_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: “Christ Died for Us” (Rom. 5:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202003_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202003/art/jwb_univ_202003_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:48</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202003_12_VIDEO" class="jsNoScroll">Robert Luccioni: “Source of Living Water” (Jer. 2:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202003_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202003/art/jwb_univ_202003_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:54</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202003_14_VIDEO" class="jsNoScroll">John Ekrann: Be Clay in Jehovah’s Hands (Rom. 12:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202002_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202002/univ/art/jwb_univ_202002_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:11</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202002_11_VIDEO" class="jsNoScroll">Hermanus van Selm: Be Faithful Like Noah (Gen. 6:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202002_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202002/art/jwb_univ_202002_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">11:27</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202002_7_VIDEO" class="jsNoScroll">M. Stephen Lett: "Guard Against Every Sort of Greed" (Jer. 45:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202002_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/202002/art/jwb_univ_202002_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:19</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202002_9_VIDEO" class="jsNoScroll">Ronald Curzan: Jehovah’s Name Is Sanctified (Matt. 6:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202001_26_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202001/univ/art/jwb_univ_202001_lss_26_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:46</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202001_26_VIDEO" class="jsNoScroll">David Schafer: Imitate Jehovah’s Generosity (1 Chron. 29:14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202001_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/202001/univ/art/jwb_univ_202001_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:16</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_202001_2_VIDEO" class="jsNoScroll">David H. Splane: Hope in the Resurrection (Heb. 11:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201912_4_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201912/art/jwb_univ_201912_lss_04_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:32</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201912_4_VIDEO" class="jsNoScroll">Patrick LaFranca: ‘Remember Those Taking the Lead’ (Heb. 13:7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201911_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201911/art/jwb_univ_201911_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:26</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201911_12_VIDEO" class="jsNoScroll">Gary Breaux: In Awe of Jehovah (Josh. 9:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201911_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201911/art/jwb_univ_201911_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:14</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201911_10_VIDEO" class="jsNoScroll">James Mantz: Jehovah Is Our Potter (Isa. 64:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201910_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201910/univ/art/jwb_univ_201910_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:16</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201910_10_VIDEO" class="jsNoScroll">M. Stephen Lett: Avoid Murmuring (Jas. 3:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201910_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201910/univ/art/jwb_univ_201910_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:45</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201910_8_VIDEO" class="jsNoScroll">Robert Ciranko: Discern Satan’s Lies (Gen. 3:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201909_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201909/univ/art/jwb_univ_201909_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:18</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201909_9_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: “Do All Things for God’s Glory” (1 Cor. 10:31)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201909_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201909/art/jwb_univ_201909_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:18</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201909_7_VIDEO" class="jsNoScroll">Gajus Glockentin: “Oppose the Devil” (Jas. 4:7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201908_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201908/univ/art/jwb_univ_201908_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:06</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201908_9_VIDEO" class="jsNoScroll">David Schafer: Every Word From Jehovah (Matt. 4:4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201907_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201907/art/jwb_univ_201907_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:35</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201907_9_VIDEO" class="jsNoScroll">Alex Reinmueller: A Balanced View of Guilt (2 Sam. 12:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201905_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201905/art/jwb_univ_201905_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:56</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201905_13_VIDEO" class="jsNoScroll">M. Stephen Lett: Pursue the Way of Love (1 John 3:18)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201905_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201905/art/jwb_univ_201905_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:10</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201905_9_VIDEO" class="jsNoScroll">William Turner, Jr.: Finding True Happiness (Matt. 5:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201904_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201904/art/jwb_univ_201904_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:17</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201904_12_VIDEO" class="jsNoScroll">Gary Breaux: Satan’s Crafty Strategy (Gen. 3:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201904_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201904/art/jwb_univ_201904_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">20:41</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201904_14_VIDEO" class="jsNoScroll">David H. Splane: Inviting All to the Memorial (Ps. 118:22)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201904_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201904/art/jwb_univ_201904_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:16</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201904_6_VIDEO" class="jsNoScroll">Mark Noumair: Show Humility (1 Pet. 5:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201904_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201904/art/jwb_univ_201904_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:56</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201904_10_VIDEO" class="jsNoScroll">Christopher Mavor: Abraham—Jehovah’s Friend (Isa. 41:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201903_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201903/art/jwb_univ_201903_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:48</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201903_12_VIDEO" class="jsNoScroll">Robert Ciranko: Jehovah Guards Loyal Ones (Ps. 97:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201903_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201903/art/jwb_univ_201903_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:52</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201903_10_VIDEO" class="jsNoScroll">Robert Luccioni: Have Humility and Peace (Phil. 2:3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201902_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201902/art/jwb_univ_201902_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:27</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201902_12_VIDEO" class="jsNoScroll">M. Stephen Lett: Pride Is Before a Crash (Prov. 16:18)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201902_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201902/art/jwb_univ_201902_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:22</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201902_10_VIDEO" class="jsNoScroll">Harold Corkern: Imitate Jesus (John 2:25)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201901_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201901/art/jwb_univ_201901_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:09</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201901_2_VIDEO" class="jsNoScroll">Mark Noumair: “This Is the Way” (Isa. 30:21)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201812_4_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201812/art/jwb_univ_201812_lss_04_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:25</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201812_4_VIDEO" class="jsNoScroll">Samuel F. Herd: Draw Close to Jehovah (Jas. 4:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201812_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201812/art/jwb_univ_201812_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:36</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201812_2_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Testing Jehovah Out (Mal. 3:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201811_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201811/art/jwb_univ_201811_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:19</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201811_11_VIDEO" class="jsNoScroll">Joel Dellinger: Strengthen Our Hope (Rev. 21:4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201811_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201811/art/jwb_univ_201811_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:44</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201811_7_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: “Continue Putting Up With One Another” (Col. 3:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201810_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201810/art/jwb_univ_201810_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">11:40</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201810_12_VIDEO" class="jsNoScroll">Kenneth Flodin: Neutral in the Ministry (Matt. 10:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201810_4_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201810/univ/art/jwb_univ_201810_lss_04_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:48</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201810_4_VIDEO" class="jsNoScroll">Robert Ciranko: God’s People Glorify His Name (1 Pet. 2:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201810_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201810/art/jwb_univ_201810_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201810_10_VIDEO" class="jsNoScroll">Gary Breaux: “Keep on the Watch” (Matt. 24:42)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201809_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201809/univ/art/jwb_univ_201809_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:31</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201809_11_VIDEO" class="jsNoScroll">Seth Hyatt: Lacking Good Sense (Prov. 5:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201809_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201809/art/jwb_univ_201809_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:30</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201809_9_VIDEO" class="jsNoScroll">James Mantz: Guard Against Greed (Luke 12:15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201808_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201808/art/jwb_univ_201808_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:39</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201808_10_VIDEO" class="jsNoScroll">Mark Sanderson: Be Prepared (Jas. 4:14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201807_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201807/art/jwb_univ_201807_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:53</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201807_11_VIDEO" class="jsNoScroll">David H. Splane: I Do Not Know You (Matt. 25:12)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201807_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201807/art/jwb_univ_201807_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:17</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201807_10_VIDEO" class="jsNoScroll">John Ekrann: "Become Imitators of God" (Eph. 5:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201806_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201806/art/jwb_univ_201806_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:37</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201806_3_VIDEO" class="jsNoScroll">William Turner, Jr.: Can Endeavors Become Distractions? (John 11:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201805_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201805/art/jwb_univ_201805_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:27</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201805_12_VIDEO" class="jsNoScroll">Robert Luccioni: Principles for Persecution (John 15:20)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201804_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201804/univ/art/jwb_univ_201804_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:09</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201804_13_VIDEO" class="jsNoScroll">Kenneth Cook, Jr.: Keep Promises, Receive Blessings (Ps. 15:4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201804_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201804/art/jwb_univ_201804_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:36</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201804_7_VIDEO" class="jsNoScroll">Mark Sanderson: “Take Your Stand Against Him” (1 Pet. 5:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201803_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201803/art/jwb_univ_201803_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:01</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201803_11_VIDEO" class="jsNoScroll">Christopher Mavor: Following Directions Saves Lives (Mark 13:19)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201803_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201803/art/jwb_univ_201803_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:58</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201803_7_VIDEO" class="jsNoScroll">Ronald Curzan: Be Acceptable to Jehovah (Eph. 5:10)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201803_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201803/art/jwb_univ_201803_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">11:04</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201803_9_VIDEO" class="jsNoScroll">Ralph Walls: Be Forgiving (Rom. 5:12)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201802_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201802/art/jwb_univ_201802_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:50</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201802_12_VIDEO" class="jsNoScroll">David Schafer: Survive the Great Day (Rev. 16:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201802_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201802/univ/art/jwb_univ_201802_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:20</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201802_8_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Be Faithful Like Abraham (Gen. 12:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201712_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201712/art/jwb_univ_201712_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:07</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201712_3_VIDEO" class="jsNoScroll">Joel Dellinger: Cannot Slave for Two Masters (Matt. 6:24)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201711_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201711/art/jwb_univ_201711_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:20</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201711_8_VIDEO" class="jsNoScroll">Gary Breaux: Reasoning on Matters (2 Thess. 2:1, 2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201711_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201711/art/jwb_univ_201711_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:31</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201711_10_VIDEO" class="jsNoScroll">Joel Dellinger: Cooperation Builds Unity (Luke 2:41)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201710_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201710/art/jwb_univ_201710_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:21</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201710_11_VIDEO" class="jsNoScroll">William Malenfant: Use Your Talents Wisely (Matt. 25:30)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201710_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201710/univ/art/jwb_univ_201710_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:39</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201710_8_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Elders Take the Lead! (Luke 8:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201710_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201710/art/jwb_univ_201710_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:50</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201710_10_VIDEO" class="jsNoScroll">Ronald Curzan: Starve Your Distraction, Feed Your Focus (Luke 12:14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201709_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201709/art/jwb_univ_201709_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:02</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201709_11_VIDEO" class="jsNoScroll">David Schafer: Micah Waited on Jehovah (Mic. 7:4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201709_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201709/art/jwb_univ_201709_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:32</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201709_10_VIDEO" class="jsNoScroll">Kenneth Flodin: Humble or Haughty? (Jas. 4:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201709_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201709/art/jwb_univ_201709_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:03</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201709_9_VIDEO" class="jsNoScroll">James Mantz: “All Things to People of All Sorts” (1 Cor. 9:22)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201708_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201708/univ/art/jwb_univ_201708_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:28</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201708_12_VIDEO" class="jsNoScroll">Mark Noumair: He Used His Body to Honor Jehovah (1 Cor. 11:24)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201708_8_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201708/univ/art/jwb_univ_201708_lss_08_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:53</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201708_8_VIDEO" class="jsNoScroll">M. Stephen Lett: Husbands, Love Your Wife as Yourself (Song of Sol. 8:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201708_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201708/univ/art/jwb_univ_201708_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:30</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201708_10_VIDEO" class="jsNoScroll">William Malenfant: Sacrifice With a Willing Attitude (Ps. 54:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201707_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201707/art/jwb_univ_201707_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:22</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201707_11_VIDEO" class="jsNoScroll">Harold Corkern: Guard Your Relationship With Jehovah (Col. 3:5)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201707_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201707/art/jwb_univ_201707_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:33</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201707_9_VIDEO" class="jsNoScroll">Seth Hyatt: Make Decisions With Jehovah (2 Chron. 16:9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201706_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201706/art/jwb_univ_201706_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:46</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201706_11_VIDEO" class="jsNoScroll">Gary Breaux: Let No One Take You Captive (Col. 2:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201706_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201706/art/jwb_univ_201706_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:25</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201706_10_VIDEO" class="jsNoScroll">M. Stephen Lett: Listen With Understanding (Matt. 13:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201706_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201706/art/jwb_univ_201706_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:30</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201706_9_VIDEO" class="jsNoScroll">William Malenfant: Morality in the Last Days (2 Tim. 3:13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_14_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201705/art/jwb_univ_201705_lss_14_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:48</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_14_VIDEO" class="jsNoScroll">Kenneth Flodin: “Better Is the End of a Matter” (Eccl. 7:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201705/art/jwb_univ_201705_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">11:22</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_13_VIDEO" class="jsNoScroll">David H. Splane: Blessings of JW.ORG (Isa. 60:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201705/art/jwb_univ_201705_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:09</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_12_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Jesus Fulfilled the Law (Matt. 5:43)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_16_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201705/art/jwb_univ_201705_lss_16_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:29</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_16_VIDEO" class="jsNoScroll">Mark Sanderson: They Would Be Objects of Persecution (Matt. 10:22)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201705/art/jwb_univ_201705_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:34</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201705_11_VIDEO" class="jsNoScroll">Mark Noumair: Pray for Integrity (Matt. 26:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201704_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201704/art/jwb_univ_201704_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:11</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201704_11_VIDEO" class="jsNoScroll">Mark Noumair: Deep Study Draws Us Close to Jehovah (Ps. 73:28)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201704_7_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201704/art/jwb_univ_201704_lss_07_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:12</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201704_7_VIDEO" class="jsNoScroll">Izak Marais: Seek First the Kingdom (Matt. 6:33)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201703_13_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201703/univ/art/jwb_univ_201703_lss_13_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:50</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201703_13_VIDEO" class="jsNoScroll">David Schafer: Jehovah Guides His People (Ps. 73:24)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201703_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201703/art/jwb_univ_201703_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:10</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201703_12_VIDEO" class="jsNoScroll">David H. Splane: Be Flexible for the Good News (1 Cor. 9:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201703_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201703/univ/art/jwb_univ_201703_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:23</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201703_11_VIDEO" class="jsNoScroll">Mark Sanderson: Jehovah Supports the Sick (Acts 15:29)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201702_10_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201702/art/jwb_univ_201702_lss_10_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:17</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201702_10_VIDEO" class="jsNoScroll">Harold Corkern: Pray for “the Peace of God” (Phil. 4:7)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201702_6_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwb/201702/univ/art/jwb_univ_201702_lss_06_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:09</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201702_6_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Why Is Neutrality So Important? (Mic. 4:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201701_12_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201701/art/jwb_univ_201701_lss_12_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:58</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201701_12_VIDEO" class="jsNoScroll">Joel Dellinger: Maintain a Waiting Attitude (Matt. 18:14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201701_11_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201701/art/jwb_univ_201701_lss_11_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:33</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201701_11_VIDEO" class="jsNoScroll">Izak Marais: “The Members . . . Are Necessary” (1 Cor. 12:22)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201701_9_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwb/univ/201701/art/jwb_univ_201701_lss_09_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:42</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwb_201701_9_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Reaching "the Most Distant Part" (Acts 1:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201612_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201612/art/jwbmw_univ_201612_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:38</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201612_1_VIDEO" class="jsNoScroll">Robert Luccioni: Don’t Limit Your Potential (Amos 7:​14)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201612_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201612/art/jwbmw_univ_201612_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:22</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201612_2_VIDEO" class="jsNoScroll">M. Stephen Lett: Show Favor to Lowly Ones (Prov. 19:17)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201611_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201611/art/jwbmw_univ_201611_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:53</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201611_1_VIDEO" class="jsNoScroll">John Ekrann: “Taste” the Ransom (Gal. 2:20)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201610_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201610/art/jwbmw_univ_201610_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:30</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201610_2_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: "A Word Spoken at the Right Time" (Prov. 15:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201610_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201610/art/jwbmw_univ_201610_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:00</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201610_1_VIDEO" class="jsNoScroll">M. Stephen Lett: Never Be a Cause for Stumbling (2 Cor. 6:3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201609_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201609/art/jwbmw_univ_201609_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:13</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201609_1_VIDEO" class="jsNoScroll">M. Stephen Lett: Win the Inner Struggle (Rom. 7:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201608_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbmw/201608/univ/art/jwbmw_univ_201608_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:09</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201608_2_VIDEO" class="jsNoScroll">Samuel F. Herd: Slave for Jehovah—A Cherished Privilege (Matt. 24:45)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201608_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201608/art/jwbmw_univ_201608_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:19</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201608_1_VIDEO" class="jsNoScroll">David H.&nbsp;Splane: Decisions of “the Faithful and Discreet Slave” (Matt. 24:45)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201607_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbmw/201607/univ/art/jwbmw_univ_201607_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:32</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201607_2_VIDEO" class="jsNoScroll">Kenneth Flodin: Beware of Deceit (Jude&nbsp;9)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201607_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201607/art/jwbmw_univ_201607_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:01</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201607_1_VIDEO" class="jsNoScroll">Mark Sanderson: Can We Speed Up His Day? (2&nbsp;Pet. 3:​11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201606_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201606/art/jwbmw_univ_201606_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:41</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201606_1_VIDEO" class="jsNoScroll">Gerrit Lösch: Do Not Hold a Grudge (1&nbsp;Cor. 13:8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201605_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201605/art/jwbmw_univ_201605_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:05</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201605_2_VIDEO" class="jsNoScroll">Samuel F. Herd: Jehovah Does Not Forget Your Love (Ps. 71:18)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201605_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201605/art/jwbmw_univ_201605_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201605_1_VIDEO" class="jsNoScroll">David Schafer: 'Practice Godly Devotion in Our Own Household' (1 Tim. 5:4)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201604_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201604/art/jwbmw_univ_201604_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:14</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201604_2_VIDEO" class="jsNoScroll">Mark Sanderson: Accept Change With Faith and Confidence (Heb. 13:17)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201603_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201603/art/jwbmw_univ_201603_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:41</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201603_3_VIDEO" class="jsNoScroll">Gary Breaux: Fighting the War Inside Us (1&nbsp;Pet. 2:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201603_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201603/art/jwbmw_univ_201603_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:30</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201603_2_VIDEO" class="jsNoScroll">Robert Ciranko: Our Faithful Older Ones (Lev. 19:32)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201603_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201603/art/jwbmw_univ_201603_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:26</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201603_1_VIDEO" class="jsNoScroll">Kenneth Flodin: "A Hiding Place From the Wind" (Isa. 32:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201602_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201602/art/jwbmw_univ_201602_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:16</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201602_3_VIDEO" class="jsNoScroll">Christopher Mavor: Young Ones Are Precious in Jehovah’s Eyes (Ps. 148:12, 13)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201602_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201602/art/jwbmw_univ_201602_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:01</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201602_2_VIDEO" class="jsNoScroll">David Schafer: Beware of Overconfidence (Matt. 26:33)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201602_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbmw/201602/univ/art/jwbmw_univ_201602_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:04</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201602_1_VIDEO" class="jsNoScroll">Robert Luccioni: Develop the Tongue of the Wise Ones (Prov. 12:18)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201601_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201601/art/jwbmw_univ_201601_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:51</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201601_1_VIDEO" class="jsNoScroll">Patrick LaFranca: Jehovah Wants Us to Be Generous (Prov. 3:27)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201512_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201512/art/jwbmw_univ_201512_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:25</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201512_3_VIDEO" class="jsNoScroll">William Malenfant: "Because You Are Righteous" (Neh. 9:7, 8)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201512_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://cms-imgp.jw-cdn.org/img/p/jwbmw/201512/univ/art/jwbmw_univ_201512_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:15</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201512_1_VIDEO" class="jsNoScroll">David H. Splane: “He Fell in Love With Her” (Gen. 24:67)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201512_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201512/art/jwbmw_univ_201512_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:43</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201512_2_VIDEO" class="jsNoScroll">Izak Marais: “When You See All These Things” (Matt. 24:33)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201511_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201511/art/jwbmw_univ_201511_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:00</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201511_2_VIDEO" class="jsNoScroll">James Mantz: “You Created All Things” (Rev. 4:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201511_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201511/art/jwbmw_univ_201511_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:57</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201511_3_VIDEO" class="jsNoScroll">Kenneth Flodin: ‘This Generation Will . . . Not Pass Away’ (Matt. 24:34)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201511_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201511/art/jwbmw_univ_201511_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:26</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201511_1_VIDEO" class="jsNoScroll">Ronald Curzan: "Let My Cry for Help Reach You" (Ps. 102:1)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201510_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201510/art/jwbmw_univ_201510_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:11</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201510_2_VIDEO" class="jsNoScroll">Alex Reinmueller: How Can We Be Fair? (Acts 10:34)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201510_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201510/art/jwbmw_univ_201510_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:19</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201510_1_VIDEO" class="jsNoScroll">Joel Dellinger: Hezekiah’s “Secret Weapon” (2&nbsp;Chron. 29:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201508_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201508/art/jwbmw_univ_201508_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:58</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201508_2_VIDEO" class="jsNoScroll">M. Stephen Lett: 'I Delight in the Law of God' (Rom. 7:22)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201508_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201508/art/jwbmw_univ_201508_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:41</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201508_1_VIDEO" class="jsNoScroll">Robert Luccioni: Do Not Love the World (1&nbsp;John 2:​15)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201507_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201507/art/jwbmw_univ_201507_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:11</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201507_2_VIDEO" class="jsNoScroll">David Schafer: “His Delight Is in the Law” (Ps. 1:2, 3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201507_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201507/art/jwbmw_univ_201507_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:34</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201507_1_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: "Consider Others Superior to You" (Phil. 2:3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201506_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201506/art/jwbmw_univ_201506_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:28</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201506_2_VIDEO" class="jsNoScroll">William Malenfant: Do Not Be Misled By the Wicked (2 Thess. 2:1, 2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201506_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201506/art/jwbmw_univ_201506_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:00</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201506_1_VIDEO" class="jsNoScroll">David H. Splane: The “Slave” Is Not 1900 Years Old (Matt. 24:45)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201505_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201505/art/jwbmw_univ_201505_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">6:59</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201505_1_VIDEO" class="jsNoScroll">Mark Sanderson: Be Willing to Open Your Hand (Prov. 3:27)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201504_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201504/art/jwbmw_univ_201504_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:35</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201504_1_VIDEO" class="jsNoScroll">David Schafer: Enduring the Imperfections of Others (Phil. 4:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201504_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201504/art/jwbmw_univ_201504_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:29</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201504_2_VIDEO" class="jsNoScroll">Gerrit Lösch: Jehovah’s Day Is Coming as a Thief (1 Thess. 5:2, 3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201503_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201503/art/jwbmw_univ_201503_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:49</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201503_2_VIDEO" class="jsNoScroll">Robert Ciranko: Do We Appreciate Our Meetings? (Ps. 27:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201503_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201503/art/jwbmw_univ_201503_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:26</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201503_1_VIDEO" class="jsNoScroll">Kenneth Flodin: “He Will Get Up Again” (Prov. 24:16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201502_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201502/art/jwbmw_univ_201502_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:07</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201502_1_VIDEO" class="jsNoScroll">David H. Splane: Unity Breaks Down Barriers (Rom. 3:29)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201502_5_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201502/art/jwbmw_univ_201502_lss_05_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">10:06</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201502_5_VIDEO" class="jsNoScroll">M. Stephen Lett: “Maintain the Oneness of the Spirit” (Eph. 4:3)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201502_4_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201502/art/jwbmw_univ_201502_lss_04_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:58</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201502_4_VIDEO" class="jsNoScroll">Geoffrey W. Jackson: Counsel That Benefits Us (Ps. 73:24)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201502_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201502/art/jwbmw_univ_201502_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:24</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201502_3_VIDEO" class="jsNoScroll">Izak Marais: What Is Faith? (John 12:42)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201502_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201502/art/jwbmw_univ_201502_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:00</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201502_2_VIDEO" class="jsNoScroll">William Malenfant: "Reflect Like Mirrors" Jehovah's Glory (2 Cor. 3:18)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201412_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201412/art/jwbmw_univ_201412_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:04</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201412_1_VIDEO" class="jsNoScroll">M. Stephen Lett: Beware of Overconfidence (1 Cor. 10:12)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201501_5_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201501/art/jwbmw_univ_201501_lss_05_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:05</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201501_5_VIDEO" class="jsNoScroll">Robert Ciranko: Marry Only in the Lord (Gen. 28:2)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201411_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201411/art/jwbmw_univ_201411_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:18</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201411_1_VIDEO" class="jsNoScroll">Kenneth Flodin: Curb Wrong Desires Immediately (Matt. 19:6)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201501_4_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201501/art/jwbmw_univ_201501_lss_04_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:52</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201501_4_VIDEO" class="jsNoScroll">Ralph Walls: "Walk as Wise Persons" (Eph. 5:15, 16)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201501_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201501/art/jwbmw_univ_201501_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">9:25</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201501_3_VIDEO" class="jsNoScroll">David Schafer: The Power of Example (Rom. 2:21)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201501_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201501/art/jwbmw_univ_201501_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:36</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201501_2_VIDEO" class="jsNoScroll">John Ekrann: “Happy Is That Slave” (Matt. 24:46)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201501_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201501/art/jwbmw_univ_201501_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:21</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201501_1_VIDEO" class="jsNoScroll">Samuel F. Herd: Older Ones—Ever Faithful (Prov. 16:31)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201410_1_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201410/art/jwbmw_univ_201410_lss_01_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">7:06</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201410_1_VIDEO" class="jsNoScroll">William Malenfant: Run the Race With Endurance (1 Cor. 9:24)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201412_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201412/art/jwbmw_univ_201412_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:48</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201412_2_VIDEO" class="jsNoScroll">Michael Hansen—Remove the Roadblock to Forgiveness (Rom. 12:19)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201412_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201412/art/jwbmw_univ_201412_lss_03_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:50</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201412_3_VIDEO" class="jsNoScroll">Geoffrey W. Jackson—Do I Conduct Myself as a Lesser One? (Rom. 14:19)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201411_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201411/art/jwbmw_univ_201411_lss_02_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:56</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201411_2_VIDEO" class="jsNoScroll">Mark Sanderson: "We Are Not Ignorant of His Designs" (2 Cor. 2:11)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201410_2_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201410/art/jwbmw_univ_201410_lss_002_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:25</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201410_2_VIDEO" class="jsNoScroll">Sam Roberson: Jehovah Loves the Humble Ones (Prov. 29:23)</a>
         </h3>
         
      </div>
   </div>




         
            
   

   
      
      
   

   

   
      
      
   

   
      
   


   

   <div class="synopsis lss desc showImgOverlay hasDuration jsLanguageAttributes dir-ltr lang-en ml-E ms-ROMAN" lang="en" xml:lang="en" dir="ltr">
      <div class="syn-img lss lg ">
         <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201410_3_VIDEO" aria-hidden="true" class="jsNoScroll">
            <img src="https://assetsnffrgf-a.akamaihd.net/assets/m/jwbmw/univ/201410/art/jwbmw_univ_201410_lss_003_lg.jpg">
            
               <div class="syn-img-overlay">
                  
                     <svg class="svg-inline--fa jwi-play fa-w-16 syn-img-overlay-icon" aria-hidden="true" focusable="false" data-prefix="jwf-jw-icons-external" data-icon="play" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-fa-i2svg=""><path fill="currentColor" d="M6.5 20a.498.498 0 01-.5-.5v-15a.5.5 0 01.735-.441l14 7.468a.5.5 0 01.002.882l-14 7.531A.5.5 0 016.5 20zM7 5.333v13.33l12.441-6.692z"></path></svg><!-- <span class="syn-img-overlay-icon jwf-jw-icons-external jwi-play"></span> -->
                  
                  
                     <span class="syn-img-overlay-text">8:41</span>
                  
               </div>
            
         </a>
      </div>
      <div class="syn-body lss">
         
         <h3>
            <a href="https://www.jw.org/en/library/videos/#en/mediaitems/VODPgmEvtMorningWorship/pub-jwbmw_201410_3_VIDEO" class="jsNoScroll">Mark Noumair: Groaning Will Be Turned Into Rejoicing (Rom. 8:22)</a>
         </h3>
         
      </div>
   </div>




         

         </div>
    """

    video_info_spanish = scrape_html(spanish_html)
    video_info_english = scrape_html(english_html)
    generate_excel(video_info_spanish, video_info_english)
