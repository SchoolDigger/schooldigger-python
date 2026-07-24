// patch-spec.js
// Patches the OpenAPI spec for cleaner SDK generation
const fs = require('fs');

const [, , inputPath, outputPath] = process.argv;
if (!inputPath || !outputPath) {
  console.error('Usage: node patch-spec.js <input.json> <output.json>');
  process.exit(1);
}

const spec = JSON.parse(fs.readFileSync(inputPath, 'utf8'));

// 1. Clean up operation IDs
const operationIdMap = {
  'Autocomplete_GetSchools23': 'autocompleteSchools',
  'Autocomplete_GetDistricts23': 'autocompleteDistricts',
  'Districts_GetAllDistricts21': 'searchDistricts',
  'Districts_GetAllDistricts24': 'searchDistricts',
  'Districts_GetDistrict21': 'getDistrict',
  'Schools_GetAllSchools22': 'searchSchools',
  'Schools_GetAllSchools24': 'searchSchools',
  'Schools_GetSchool22': 'getSchool',
  'Rankings_GetSchoolRank21': 'getSchoolRankings',
  'Rankings_GetRank_District': 'getDistrictRankings',
};

for (const [path, methods] of Object.entries(spec.paths || {})) {
  for (const [method, operation] of Object.entries(methods)) {
    if (typeof operation !== 'object' || !operation.operationId) continue;

    // Rename operation ID
    if (operationIdMap[operation.operationId]) {
      operation.operationId = operationIdMap[operation.operationId];
    }

    // Remove appID and appKey from per-endpoint parameters
    // (they'll be handled by the security scheme instead)
    if (Array.isArray(operation.parameters)) {
      operation.parameters = operation.parameters.filter(
        p => p.name !== 'appID' && p.name !== 'appKey'
      );
    }
  }
}

// 2. Add security schemes
if (!spec.components) spec.components = {};
spec.components.securitySchemes = {
  appID: { type: 'apiKey', in: 'query', name: 'appID' },
  appKey: { type: 'apiKey', in: 'query', name: 'appKey' }
};
spec.security = [{ appID: [], appKey: [] }];

// 3. Set metadata
spec.info.title = 'SchoolDigger API';
spec.info.description = 'K-12 school and district data for 120,000+ U.S. schools';
spec.info.contact = {
  name: 'SchoolDigger API Support',
  email: 'api@schooldigger.com',
  url: 'https://developer.schooldigger.com'
};

fs.writeFileSync(outputPath, JSON.stringify(spec, null, 2));
console.log(`Patched spec written to ${outputPath}`);
