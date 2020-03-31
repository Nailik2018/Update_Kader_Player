# -*- coding: utf-8 -*-

from Collections.MttvKader import MttvKader

csv_male_download_link = "http://www.click-tt.ch/cgi-bin/WebObjects/nuLigaTTCH.woa/wa/eloRankingsCSV?gender=male"
csv_female_download_link = "http://www.click-tt.ch/cgi-bin/WebObjects/nuLigaTTCH.woa/wa/eloRankingsCSV?gender=female"

mttv_kader = MttvKader(csv_male_download_link, csv_female_download_link)
mttv_kader.update_execute()