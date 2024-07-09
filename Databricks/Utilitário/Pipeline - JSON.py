# Databricks notebook source
resources:
  jobs:
    Pipeline_Medallion_Architecture:
      name: Pipeline - Medallion Architecture
      tasks:
        - task_key: Games_Bronze_to_Silver
          notebook_task:
            notebook_path: /Repos/jpedropuc@gmail.com/ProjetoMVPBancodeDados/Databricks/1.
              Bronze to Silver/TWIC - Games/bronze to silver - games root
            source: WORKSPACE
          existing_cluster_id: 0613-232255-noxfkz06
        - task_key: Players_Bronze_to_Silver
          notebook_task:
            notebook_path: /Repos/jpedropuc@gmail.com/ProjetoMVPBancodeDados/Databricks/1.
              Bronze to Silver/FIDE - Players/bronze to silver - players root
            source: WORKSPACE
          existing_cluster_id: 0613-232255-noxfkz06
        - task_key: Games_Common_Openings
          depends_on:
            - task_key: Games_Bronze_to_Silver
            - task_key: Players_-_Current_Month_Bronze_to_Silver
          notebook_task:
            notebook_path: /Repos/jpedropuc@gmail.com/ProjetoMVPBancodeDados/Databricks/2.
              Silver to Gold/TWIC - Games/silver to gold - matchs common
              openings
            source: WORKSPACE
          existing_cluster_id: 0613-232255-noxfkz06
        - task_key: Mix_federation_evolution_by_time
          depends_on:
            - task_key: Players_Bronze_to_Silver
          notebook_task:
            notebook_path: /Repos/jpedropuc@gmail.com/ProjetoMVPBancodeDados/Databricks/2.
              Silver to Gold/FIDE - Players/Mix/silver to gold - fed ranking
              evolution by time
            source: WORKSPACE
          existing_cluster_id: 0613-232255-noxfkz06
        - task_key: Players_-_Current_Month_Bronze_to_Silver
          depends_on:
            - task_key: Players_Bronze_to_Silver
          notebook_task:
            notebook_path: /Repos/jpedropuc@gmail.com/ProjetoMVPBancodeDados/Databricks/1.
              Bronze to Silver/FIDE - Players/bronze to silver - players current
              month
            source: WORKSPACE
          existing_cluster_id: 0613-232255-noxfkz06
        - task_key: Female_base_filter_current_month
          depends_on:
            - task_key: Players_-_Current_Month_Bronze_to_Silver
          notebook_task:
            notebook_path: /Repos/jpedropuc@gmail.com/ProjetoMVPBancodeDados/Databricks/2.
              Silver to Gold/FIDE - Players/Female_filter_base
            source: WORKSPACE
          existing_cluster_id: 0613-232255-noxfkz06
        - task_key: Female_WGM_count_avg_rating
          depends_on:
            - task_key: Female_base_filter_current_month
          notebook_task:
            notebook_path: /Repos/jpedropuc@gmail.com/ProjetoMVPBancodeDados/Databricks/2.
              Silver to Gold/FIDE - Players/Female/silver to gold - WGM count
              avg. rating
            source: WORKSPACE
          existing_cluster_id: 0613-232255-noxfkz06
        - task_key: Female_federation_avg_rating
          depends_on:
            - task_key: Female_base_filter_current_month
          notebook_task:
            notebook_path: /Repos/jpedropuc@gmail.com/ProjetoMVPBancodeDados/Databricks/2.
              Silver to Gold/FIDE - Players/Female/silver to gold - fed avg.
              rating
            source: WORKSPACE
          existing_cluster_id: 0613-232255-noxfkz06
        - task_key: Female_over_2300_rating_count
          depends_on:
            - task_key: Female_base_filter_current_month
          notebook_task:
            notebook_path: /Repos/jpedropuc@gmail.com/ProjetoMVPBancodeDados/Databricks/2.
              Silver to Gold/FIDE - Players/Female/silver to gold - >2300 rating
              count
            source: WORKSPACE
          existing_cluster_id: 0613-232255-noxfkz06
        - task_key: Female_under_20_rating
          depends_on:
            - task_key: Female_base_filter_current_month
          notebook_task:
            notebook_path: /Repos/jpedropuc@gmail.com/ProjetoMVPBancodeDados/Databricks/2.
              Silver to Gold/FIDE - Players/Female/silver to gold - <20 avg.
              rating
            source: WORKSPACE
          existing_cluster_id: 0613-232255-noxfkz06
        - task_key: Male_base_filter_current_month
          depends_on:
            - task_key: Players_-_Current_Month_Bronze_to_Silver
          notebook_task:
            notebook_path: /Repos/jpedropuc@gmail.com/ProjetoMVPBancodeDados/Databricks/2.
              Silver to Gold/FIDE - Players/Male_filter_base
            source: WORKSPACE
          existing_cluster_id: 0613-232255-noxfkz06
        - task_key: Male_GM_count_avg_rating
          depends_on:
            - task_key: Male_base_filter_current_month
          notebook_task:
            notebook_path: /Repos/jpedropuc@gmail.com/ProjetoMVPBancodeDados/Databricks/2.
              Silver to Gold/FIDE - Players/Male/silver to gold - count GM avg.
              rating
            source: WORKSPACE
          existing_cluster_id: 0613-232255-noxfkz06
        - task_key: Male_federation_avg_rating
          depends_on:
            - task_key: Male_base_filter_current_month
          notebook_task:
            notebook_path: /Repos/jpedropuc@gmail.com/ProjetoMVPBancodeDados/Databricks/2.
              Silver to Gold/FIDE - Players/Male/silver to gold - fed avg.
              rating
            source: WORKSPACE
          existing_cluster_id: 0613-232255-noxfkz06
        - task_key: Male_over_2600_rating_count
          depends_on:
            - task_key: Male_base_filter_current_month
          notebook_task:
            notebook_path: /Repos/jpedropuc@gmail.com/ProjetoMVPBancodeDados/Databricks/2.
              Silver to Gold/FIDE - Players/Male/silver to gold - >2600 rating
              count
            source: WORKSPACE
          existing_cluster_id: 0613-232255-noxfkz06
        - task_key: Male_under_20_rating
          depends_on:
            - task_key: Male_base_filter_current_month
          notebook_task:
            notebook_path: /Repos/jpedropuc@gmail.com/ProjetoMVPBancodeDados/Databricks/2.
              Silver to Gold/FIDE - Players/Male/silver to gold - <20 avg.
              rating
            source: WORKSPACE
          existing_cluster_id: 0613-232255-noxfkz06
      queue:
        enabled: true

