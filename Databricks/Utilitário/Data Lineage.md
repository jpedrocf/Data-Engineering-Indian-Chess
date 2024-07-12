```mermaid

flowchart TD

    A[["<a rel="noopener" href="https://ratings.fide.com/download_lists.phtml" target="_blank">FIDE DB</a>"]] -- Python Script --> C[("Databricks DB")]
    B[["<a rel="noopener" href="https://theweekinchess.com/twic" target="_blank">TWIC - The Week in Chess</a>"]] -- Python Script --> C
    C -- Create DB --> D[("players_complete")] & E[("event_games")]
    C -- Default --> K[("current_month_players")]
    K -- Monthly Update --> D
    D -- Backup --> Z[("players_complete_bckup")]
    D -- ETL --> F[("players")] & L[("players_current_month")]
    E -- ETL --> G[("event_games")]
    F -- ETL --> H[("Mix_fed_rank_evolution")] & M[("Mix_ind_rank_evolution")]
    L -- ETL --> I[("male_current_month_base")] & J[("female_current_month_base")] & V[("IND_most_ef_openings")] & X[("IND_world_comp_openings")] & Y[("games_with_country")]
    I -- ETL --> N[("M_20_average_rating_by_country")] & O[("m_2600_rated_players_per_country")] & P[("M_GM_average_rating_by_country")] & U[("m_top10_average_rating_by_country")]
    J -- ETL --> Q[("f_20_average_rating")] & R[("F_2300_rated_players_per_country")] & S[("f_top10_average_rating_by_country")] & T[("f_WGM_average_rating_by_country")]
    G -- ETL --> V & X & Y



    style D color:#FFFFFF, fill:#CD7F32, stroke:#FF6D00,stroke:#FFFFFF
    style E color:#FFFFFF, fill:#CD7F32, stroke:#FF6D00,stroke:#FFFFFF
    style Z color:#FFFFFF, fill:#CD7F32, stroke:#FF6D00,stroke:#FFFFFF
    style F color:#FFFFFF, fill:#C0C0C0, stroke:#FF6D00,stroke:#FFFFFF
    style L color:#FFFFFF, fill:#C0C0C0, stroke:#FF6D00,stroke:#FFFFFF
    style G color:#FFFFFF, fill:#C0C0C0, stroke:#FF6D00,stroke:#FFFFFF
    style H color:#FFFFFF, fill:#FFD700, stroke:#FF6D00,stroke:#FFFFFF
    style M color:#FFFFFF, fill:#FFD700, stroke:#FF6D00,stroke:#FFFFFF
    style I color:#FFFFFF, fill:#C0C0C0, stroke:#FF6D00,stroke:#FFFFFF
    style J color:#FFFFFF, fill:#C0C0C0, stroke:#FF6D00,stroke:#FFFFFF
    style Y color:#FFFFFF, fill:#C0C0C0, stroke:#FF6D00,stroke:#FFFFFF
    style V color:#FFFFFF, fill:#FFD700, stroke:#FF6D00,stroke:#FFFFFF
    style X color:#FFFFFF, fill:#FFD700, stroke:#FF6D00,stroke:#FFFFFF
    style N color:#FFFFFF, fill:#FFD700, stroke:#FF6D00,stroke:#FFFFFF
    style O color:#FFFFFF, fill:#FFD700, stroke:#FF6D00,stroke:#FFFFFF
    style P color:#FFFFFF, fill:#FFD700, stroke:#FF6D00,stroke:#FFFFFF
    style U color:#FFFFFF, fill:#FFD700, stroke:#FF6D00,stroke:#FFFFFF    
    style Q color:#FFFFFF, fill:#FFD700, stroke:#FF6D00,stroke:#FFFFFF
    style R color:#FFFFFF, fill:#FFD700, stroke:#FF6D00,stroke:#FFFFFF
    style S color:#FFFFFF, fill:#FFD700, stroke:#FF6D00,stroke:#FFFFFF
    style T color:#FFFFFF, fill:#FFD700, stroke:#FF6D00,stroke:#FFFFFF
