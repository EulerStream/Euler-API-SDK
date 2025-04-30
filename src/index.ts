import {AccountsApi, AlertsApi, AnalyticsApi, AuthenticationApi, TikTokApi, WebcastApi} from "@/sdk";
import {buildConfig, ClientConfiguration} from "@/utils";

// Exports
export * from './sdk';
export * from './utils';

// Export an API Client
export default class EulerStreamApiClient {

  public readonly tiktok: TikTokApi;
  public readonly webcast: WebcastApi;
  public readonly accounts: AccountsApi;
  public readonly authentication: AuthenticationApi;
  public readonly analytics: AnalyticsApi;
  public readonly alerts: AlertsApi;
  public readonly alertTargets: AlertsApi;
  public readonly configuration: ClientConfiguration;

  /**
   * EulerStream API Client
   *
   * Configuration
   *
   *
   * API Instances
   *
   * @param config The configuration for the API client
   */
  constructor(
      config: Partial<ClientConfiguration> = {}
  ) {

    // Build the config
    this.configuration = buildConfig(config);

    // Set up the APIs
    this.tiktok = new TikTokApi(this.configuration);
    this.webcast = new WebcastApi(this.configuration);
    this.accounts = new AccountsApi(this.configuration);
    this.authentication = new AuthenticationApi(this.configuration);
    this.analytics = new AnalyticsApi(this.configuration);
    this.alerts = new AlertsApi(this.configuration);
    this.alertTargets = new AlertsApi(this.configuration);

  }

}


