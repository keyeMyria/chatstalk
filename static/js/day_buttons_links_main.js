$(document).ready(function(){var selected_year,selected_month,selected_day;$('.btn_to_click').click(function(e){e.preventDefault();selected_year=$("#select_year option:selected").val();selected_month=$("#select_month option:selected").val();selected_day=$("#select_day option:selected").val();if(selected_year!="non_year"&&selected_month!="non_month"&&selected_day!="non_day"){var target_day=$(this).attr('data-sj-td');var target_month=$(this).attr('data-sj-tm');var target_year=$(this).attr('data-sj-ty');var by,bm,bd,ty,tm,td;by=parseInt(selected_year).toString(16);bm=parseInt(selected_month).toString(16);bd=parseInt(selected_day).toString(16);ty=parseInt(target_year).toString(16);tm=parseInt(target_month).toString(16);td=parseInt(target_day).toString(16);var selected_lang=$("#select_lang option:selected").val();var url_default;switch(selected_lang){case'non_lang':url_default=$('#url_day').attr('data-sj');break;case'ara':url_default=$('#url_day_ara').attr('data-sj');break;case'chi':url_default=$('#url_day_chi').attr('data-sj');break;case'eng':url_default=$('#url_day_eng').attr('data-sj');break;case'por':url_default=$('#url_day_por').attr('data-sj');break;case'spa':url_default=$('#url_day_spa').attr('data-sj');break;default:url_default=$('#url_day').attr('data-sj');break}var link_text=url_default+"?d="+by+"_"+bm+"_"+bd+"_"+ty+"_"+tm+"_"+td;location.href=link_text}else{$("#p_birth_warning").html($('#phrase_birthday').attr('data-sj'))}})});